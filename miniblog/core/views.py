from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Function to Display the Home Page of the WebSite
def Home(request : HttpRequest) -> HttpResponse:
    '''
        Function to display the Home Page of the Project
        Note: Do not make any changes let the page be GET, as the initial request is always GET. Let it be static
    '''
    return render(request, 'core/home.html')

# Function to Display the About Page of the WebSite 
def About(request : HttpRequest) -> HttpResponse:
    '''
        About Page!
        Mostly Static
    '''
    return render(request, 'core/about.html')

# Function to Display the Contact Page of the WebSite 
def Contact(request : HttpRequest) -> HttpResponse:
    '''
        Make sure to configure the SMTP as for your email in the settings.py file
        Request == POST -> Validate the Contact Form and send the Mail
        Request == GET -> Render the Form Fields to the user!
    '''
    return render(request, 'core/contact.html')

# Function for Sign Up 
def SignUP(request : HttpRequest) -> HttpResponse:
    '''
        Using Django's Authentication System!
        Model Made out of Abstract User so is needed more fields? Then add in the user application's models.py file it!
    '''
    return render(request, 'core/signup.html')

# Function for Log In
def LogIn(request : HttpRequest) -> HttpResponse:
    '''
        Also using Django's Authentication System!
        Request == POST -> Validate the fields and is correct then login & redirect to User Home Page!
        Request == GET -> Render the LogIn Form

        If any mistake in error or Form not validated then render the Same Page!
    '''
    return render(request, 'core/login.html')

def LogOut(request : HttpRequest) -> HttpResponse:
    '''
        Using Django's Authentication System!
        Clearing the Session!
    '''
    if request.user.is_authenticated:
        logout(request.user)
    return HttpResponseRedirect('/')