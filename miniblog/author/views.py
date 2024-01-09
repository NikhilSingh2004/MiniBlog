from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Function to Display the Home Page of the Author
def AuthorHome(request : HttpRequest) -> HttpResponse:
    '''
        First Check if the User is_Author, if True let the user Access the Home Page of the AuthHome,
        Else HttpResponseRedirect the User to Be_Author Page!.

        If Already a Author, then fetch all the Blog Model Row that have the Author's User ID and Display them, with Pagination
    '''
    return HttpResponse("This is the Author Home Page!")

def BeAuthor(request : HttpRequest) -> HttpResponse:
    '''
        First Check if the User is authenticated!.
        If the Request is an POST request then Validate the Fields and if all fine then make the User a Author
        If an GET request then render the Form to become Author
    '''
    return HttpResponse("The Form Page to Become an Author!")

# Function to Add Another Blog in the DataBase
def AddBlog(request : HttpRequest) -> HttpResponse:
    '''
        First Check if the User is authenticated and the User is an Author, If yes then Proceed
        If the request is GET -> Display the Form itself!
        If POST -> Validate all the Fields data and is all good then create a Blog Model Object and Save it!
    '''
    return HttpResponse("The Form Page to Add an Blog!")

# Function to Edit a Specific Blog
def EditBlog(request : HttpRequest) -> HttpResponse:
    '''
        First Validate the User to be Authenticated and is_Author, is yes then Proceed.
        If the request is GET -> Initialize the Form with the perticular blog object.
        If the request is POST -> Validate the Form and Save!
    '''
    return HttpResponse("The Form Page to Edit an Blog!")

# Function to Delete a Specific Blog
def DeleteBlog(request : HttpRequest, id : int) -> HttpResponse:
    '''
        First Check if User is Authenticated and is_Author, if yes then delete the Blog
    '''
    return HttpResponse("Function to Delete a Blog")