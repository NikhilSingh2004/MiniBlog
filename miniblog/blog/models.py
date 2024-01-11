from django.db import models
from datetime import datetime
# Model For Blog
'''
    The Model Should Consist of these Fields:
        Date - DateTimeField, Upload Date of the Blog.
        User (Foreign) - User Model Field
        Title - Title Char Field
        Content - TextArea Field
    
    Can Add more content if needed!.
'''

'''

class Blog(models.Model):
    pass
    
'''

class Blog(models.Model):
    user = models.OneToOneField('user.M_User', on_delete=models.CASCADE)

    date = models.DateTimeField(default=datetime.now())

    title = models.CharField(max_length=1024, null=True)

    Content = models.TextField(null=True)
