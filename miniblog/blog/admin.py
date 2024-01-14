from django.contrib import admin
from . models import Blog

class Model_Blog(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'author',
        'date'
    ]

admin.site.register(Blog, Model_Blog)