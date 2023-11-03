
from django.shortcuts import HttpResponseRedirect,render,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_login.models import Follow
from App_posts.models import Post,Like


@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user)
    posts=Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    if request.method=='GET':
        search=request.GET.get('search','')
        result=User.objects.filter(username__icontains=search)
    return render(request,'App_posts/home.html',context={'title':'Home','search':search,'result':result,'posts':posts,'liked_post_list':liked_post_list})

@login_required
def liked(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse("Home"))

@login_required
def unliked(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse("Home"))