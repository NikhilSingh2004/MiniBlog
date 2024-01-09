from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('signUp/', views.SignUP, name='SignUp'),
    path('logIn/', views.LogIn, name='LogIn'),
    path('blogs/', include('blog.urls')),
]
