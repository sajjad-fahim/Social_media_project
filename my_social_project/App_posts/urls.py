from App_posts import views
from django.urls import path
app_name='App_posts'

urlpatterns=[


    path('',views.home,name="Home"),
    path('liked/<pk>',views.liked,name='Like'),
    path('unliked/<pk>',views.unliked,name='Unlike'),
]