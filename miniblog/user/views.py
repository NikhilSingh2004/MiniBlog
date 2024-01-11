from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# User Home
def UserHome(request : HttpRequest) -> HttpResponse:
    '''
        First Check is the request.user is Authenticated, if yes the render the User Home Page!.
        The User Home Page Should Consist of all the Blog's the User have saved
    '''
    return HttpResponse("This is the User Home Page!")

def EditUser(request : HttpRequest) -> HttpResponse:
    '''
        Check for Authentication, if yes proceed.
        If the request is GET -> Initialize the Edit Form with User Object and Render
        If the request is POST -> Load the Data & Validate the Input Data, is all good then Save
    '''
    return HttpResponse("This is the Edit Page of the user with the Object being initialized!")

def DeleteUser(request :  HttpRequest) -> HttpResponse:
    '''
        Function to delete the user. First Make sure the user is authenticated 
        Do not do hard delete! Make a soft delete
    '''
    return HttpResponse("This is the Delete User Function")