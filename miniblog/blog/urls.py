from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome, name='BlogHome'),
    path('<slug:blog>/', views.OneBlog, name='OneBlog'),
    path('save/<int:id>', views.SaveBlog, name='SaveBlog'),
]
