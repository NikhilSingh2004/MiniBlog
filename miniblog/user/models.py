from django.db import models
from django.contrib.auth.models import AbstractUser
# User Model with Extended Capablity
'''
    To Extend fields in the Defaul User Model, use AbstractUser Model

    Extended Fields

        is_author - Boolean Field that will indicated wether the User is an Author or Not
        
        saved_blogs - One-To-Many Relation, Foreign Field that will store all array of Blogs the User have Saved for Later read!.

    To eliminate Circular Import In Blog and User Model Using `swapped`!
'''

class M_User(AbstractUser):
    is_author = models.BooleanField(default=False)

    saved_blogs = models.ManyToManyField('blog.Blog', related_name='saved_by_users', blank=True)

    # Specify unique related_name values for groups and user_permissions
    groups = models.ManyToManyField('auth.Group', related_name='m_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='m_user_permissions', blank=True)