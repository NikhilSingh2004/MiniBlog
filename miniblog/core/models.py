from django.db import models

'''
    Create Contact Us Model

    Fields :
        first_name -> Char Field with max_length = 128

        last_name -> Char Field with max_length = 128 

        Username -> Char Field with max_length = 128 , null = True , blank = True

        email -> Email Field with max_length = 256

        body -> Text Field 

        footer -> Text Filed , null = True , blank = True
'''

class ContactUs(models.Model):
    
    first_name = models.CharField(max_length=128)

    last_name = models.CharField(max_length=128)

    username = models.CharField(max_length=128, null=True, blank=True)

    email = models.CharField(max_length=256)

    body = models.TextField()

    footer = models.TextField(max_length=128, null=True, blank=True)