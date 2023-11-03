from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from App_login.models import UserProfile


class UserRegistration(UserCreationForm):
    email=forms.EmailField(required=True ,label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True ,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True ,label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True ,label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))


    class Meta:
        model=User
        fields=('email',"username",'password1','password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class EditProfile(forms.ModelForm):
    date_of_birth=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=UserProfile()
        exclude=('user',)




    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'first_name', 'last_name']

    # def clean_password_confirm(self):
    #     # Check if the password and password confirmation match
    #     password = self.cleaned_data.get('password')
    #     password_confirm = self.cleaned_data.get('password_confirm')
    #     if password and password_confirm and password != password_confirm:
    #         raise forms.ValidationError("Passwords do not match.")
    #     return password_confirm

    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user

