from django.urls import path
from App_login import views

app_name="App_login"

urlpatterns=[

   path('register/',views.register,name="Register"),
   path('login/',views.user_login,name="Login"),
   path('edit/',views.edit_profile,name="Edit"),
   path('logout/',views.logout_user,name="Logout"),
   path('profile/',views.profile,name="Profile"),
   path('user/<username>/',views.user,name="User"),
   path('follow/<username>/',views.follow,name="Follow"),
   path('unfollow/<username>/',views.unfollow,name="Unfollow"),



]
