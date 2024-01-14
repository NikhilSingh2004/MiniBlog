from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('signup/', views.SignUP, name='SignUp'),
    path('login/', views.LogIn, name='LogIn'),
    path('logout/', views.LogOut, name='LogOut'),
    path('changepassword/', views.ChangePassword, name='ChangePass'),
]
