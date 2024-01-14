from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome, name='BlogHome'),
    path('<str:slug>/', views.OneBlog, name='OneBlog'),
    path('save/<str:slug>', views.SaveBlog, name='SaveBlog'), # To Save a Specific Blog (Incomplete)
]
