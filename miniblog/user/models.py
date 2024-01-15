from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model with Extended Capablity

'''

    If there are no solution to this problem with change in the settings.py file then i would have to shift the user_M_User to auth_user and add the user_M_User extra fields to the auth_user model and use it

    To Extend fields in the Defaul User Model, use AbstractUser Model

    Extended Fields

        is_author -> Boolean Field that will indicated wether the User is an Author or Not
        
        saved_blogs -> One-To-Many Relation, Foreign Field that will store all array of Blogs the User have Saved for Later read!.

        is_deleted -> For Soft delete of the user
        
    To eliminate Circular Import In Blog and User Model Using `swapped`!
'''

class M_User(AbstractUser):
    is_author = models.BooleanField(default=False)

    saved_blogs = models.ManyToManyField('blog.Blog', related_name='saved_by_users', blank=True)

    is_deleted = models.BooleanField(default=False)

    # Specify unique related_name values for groups and user_permissions
    groups = models.ManyToManyField('auth.Group', related_name='m_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='m_user_permissions', blank=True)