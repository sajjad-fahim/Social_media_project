from django.shortcuts import render,reverse,redirect,HttpResponseRedirect
from App_login.forms import UserRegistration,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from App_login.models import UserProfile,Follow
from django.contrib.auth.decorators import login_required
from App_login.forms import EditProfile
from App_posts.forms import PostForm
from django.contrib.auth.models import User


def register(request):
    form=UserRegistration()
    registered=False
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            registered=True
            user_profile=UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_login:Login'))
    
    dict={'form':form,'registered':registered}
    return render(request,'App_login/registration.html',context=dict)



def user_login(request):
    form=UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_posts:Home'))
                
    return render(request, 'App_login/login.html', context={'title':'Login','form':form})


@login_required
 
def edit_profile(request):
    try:
        current_user = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        current_user = UserProfile(user=request.user)
    form=EditProfile(instance=current_user)
    if request.method=="POST":
        form=EditProfile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form=EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:Profile'))

    return render(request,'App_login/profile.html',context={'form':form,'title':'Edit Profile social'})


@login_required 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:Login'))


@login_required
def profile(request):
    form=PostForm()
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return HttpResponseRedirect(reverse("Home"))

    return render(request,'App_login/user.html',context={'title':'Post','form':form})

@login_required

def user(request,username):
    user_other=User.objects.get(username=username)
    already_followed=Follow.objects.filter(follower=request.user,following=user_other)
    if user_other==request.user:
        return HttpResponseRedirect(reverse('App_login:Profile'))
    
    return render(request,'App_login/other_user.html',context={'user_other':user_other,'already_followed':already_followed})


@login_required

def follow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user, created = Follow.objects.get_or_create(follower=follower_user, following=following_user)
    return HttpResponseRedirect(reverse('App_login:User',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=Follow.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_login:User',kwargs={'username':username}))