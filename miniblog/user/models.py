from django.db import models

# User Model with Extended Capablity
'''
    To Extend fields in the Defaul User Model, use AbstractUser Model

    Extended Fields

        is_author - Boolean Field that will indicated wether the User is an Author or Not
        
        saved_blogs - One-To-Many Relation, Foreign Field that will store all array of Blogs the User have Saved for Later read!.

    To eliminate Circular Import In Blog and User Model Using `swapped`!
'''

