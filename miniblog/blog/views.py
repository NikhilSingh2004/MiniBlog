from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Function to Display the Home Page of the blog application, Here all the Available blogs will be shown in Descending manner
def BlogHome(request : HttpRequest) -> HttpResponse:
    '''
        The Function will Display all the Available Blogs in the Blog Model `objects.all()`.
        There should be Pagination while displaying the blogs!.
    '''
    return HttpResponse("This Here all the blogs will be shown!") 

# Function to Display One Specific Blog Selected To Read
def OneBlog(request : HttpRequest) -> HttpResponse:
    '''
        Function to Display a Specific Blog.
        Need to Make sure the Blog Title is shown in the URL (Slug Format).
    '''
    return HttpResponse("This Here all the blogs will be shown!") 

# Save Blog
def SaveBlog(request : HttpRequest) -> HttpResponse:
    '''
        First Authenticate the User and is yes, then add the blog object of the saved_blogs field.
        And Redirect the User to the page where the user was!.
    '''
    return HttpResponse("This is the Save Blog Function")