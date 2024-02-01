from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Mini Blog Admin Dashboard"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to MiniBlog Admin Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('user.urls')),
    # path('author/', include('author.urls')),
]
