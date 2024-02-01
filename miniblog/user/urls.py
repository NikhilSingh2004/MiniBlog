from django.urls import path
from . import views
urlpatterns = [
    # Paths for User
    path('', views.UserHome, name='UserHome'),
    path('edit/<int:id>', views.EditUser, name='EditUser'),
    path('delete/<int:id>', views.DeleteUser, name='DeleteUser'),

    # Paths for Author
    path('add/', views.AddBlog, name='AddBlog'),
    path('edit/', views.EditBlog, name='EditBlog'), # Make a Slug at the end of the URL with the Blog Title
    path('delete/<int:id>', views.DeleteBlog, name='DeleteBlog'),
    path('beAuthor/', views.BeAuthor, name='BecomeAuthor'), # Make a Slug at the end of the URL with the User Name
    path('deleteAuthor/', views.DeleteAuthor, name='DeleteAuthor'), # To Delete the Author Account
]
