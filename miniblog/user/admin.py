from django.contrib import admin
from . models import M_User

class Model_User(admin.ModelAdmin):
    list_display = [
        'id', 
        'username' , 
        'email', 
        'is_author'
    ]

admin.site.register(M_User, Model_User)