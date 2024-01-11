from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('edit/<int:id>', views.EditUser, name='EditUser'),
    path('delete/<int:id>', views.DeleteUser, name='DeleteUser'),
]
