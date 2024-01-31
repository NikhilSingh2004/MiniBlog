from blog.models import Blog
from user.models import M_User
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm, AuthenticateM_UserForm, CustomPasswordChangeForm, FormContactUs

# Function to Display the Home Page of the WebSite
def Home(request : HttpRequest) -> HttpResponse:
    '''
        Function to display the Home Page of the Project
        Note: Do not make any changes let the page be GET, as the initial request is always GET. Let it be static
    '''
    Blog_list = Blog.objects.all().order_by('id') 
    paginator = Paginator(Blog_list, 5)
    page = request.GET.get('page', 1)
    blogs = None
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    if request.user.is_authenticated:
        context ={
            'loged_in' : True,
            'blogs' : blogs
        }
        return render(request, 'core/home.html', context)
    context ={
        'sign_log' : True,
        'blogs' : blogs
    }
    return render(request, 'core/home.html', context)

# Function to Display the About Page of the WebSite 
def About(request : HttpRequest) -> HttpResponse:
    '''
        About Page!
        Mostly Static
    '''
    if request.user.is_authenticated:
        return render(request, 'core/about.html', {'loged_in' : True})
    return render(request, 'core/about.html', {'sign_log' : True})

# Function to Display the Contact Page of the WebSite 
def Contact(request : HttpRequest) -> HttpResponse:
    '''
        Make sure to configure the SMTP as for your email in the settings.py file
        Request == POST -> Validate the Contact Form and send the Mail
        Request == GET -> Render the Form Fields to the user!
    '''
    form = FormContactUs()
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                form = FormContactUs(data = request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Mail Sent Successfuly!")
                    return HttpResponseRedirect('/')
                messages.error(request, "Please Enter Correct Details!")
                return render(request, 'core/contact.html', {'loged_in' : True, 'form' : form})
            except Exception as e:
                print(e.__str__())
                messages.error(request, "Something Went Wrong!")
                return HttpResponseRedirect('/')
        return render(request, 'core/contact.html', {'loged_in' : True, 'form' : form})
    messages.error(request, "Please LogIn!")
    return render(request, 'core/contact.html', {'sign_log' : True, 'form' : form})

# Function for Sign Up 
def SignUP(request : HttpRequest) -> HttpResponse:
    '''
        Using Django's Authentication System!
        Model Made out of Abstract User so is needed more fields? Then add in the user application's models.py file it!
    '''
    if not request.user.is_authenticated:
        form = SignUpForm()
        if request.method == "POST":
            try:
                form = SignUpForm(data=request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Sign Up Successful!")
                    return HttpResponseRedirect('/')
                messages.error(request, "Something Went Wrong!")
                form = SignUpForm()
                return render(request, 'core/signup.html', {'form' : form, 'sign_log' : False})
            except Exception as e:
                print(e.__str__())
                return render(request, 'core/signup.html', {'form' : form, 'sign_log' : False})
        else:
            return render(request, 'core/signup.html', {'form' : form, 'sign_log' : False})

# Function for Log In
def LogIn(request: HttpRequest) -> HttpResponse:
    '''
        Also using Django's Authentication System!
        Request == POST -> Validate the fields and is correct then login & redirect to User Home Page!
        Request == GET -> Render the LogIn Form

        If any mistake in error or Form not validated then render the Same Page!
    '''
    form = AuthenticateM_UserForm()

    if not request.user.is_authenticated:
        if request.method == "POST":
            try:
                fm = AuthenticateM_UserForm(data=request.POST)
                if fm.is_valid():
                    username = fm.cleaned_data['username']
                    password = fm.cleaned_data['password']
                    user = authenticate(username=username, password=password, is_deleted=False)
                    
                    if user:
                        login(request=request, user=user)
                        messages.success(request, "Log In Successful")
                        return HttpResponseRedirect('/')
                    else:
                        form.add_error(None, 'Invalid username or password')
                return render(request, 'core/login.html', {'form': form, 'sign_log' : False})
            except Exception as e:
                print(e.__str__())
                return render(request, 'core/login.html', {'form': form, 'sign_log' : False})
        else:
            return render(request, 'core/login.html', {'form': form, 'sign_log' : False})
    else:
        return HttpResponseRedirect('/')

# Function to Log Out the User
def LogOut(request: HttpRequest) -> HttpResponse:
    '''
        Using Django's Authentication System!
        Clearing the Session!
    '''
    if request.user.is_authenticated:
        try:
            logout(request)
            messages.success(request, "Log Out Successful")
        except Exception as e:
            print(e.__str__())
    return HttpResponseRedirect('/')

# Function to Change User Password
def ChangePassword(request: HttpRequest) -> HttpResponse:
    '''
        Function to Let Users Change Their password

        Request == POST -> Validate The Change Password Form
        Request == GET -> Render the Change Password Form (But only if the user is authenticated!)
    '''
    if request.user.is_authenticated:
        form = CustomPasswordChangeForm(user=request.user)
        if request.method == "POST":
            try:
                form = CustomPasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save() 
                    update_session_auth_hash(request, form.user)
                    print('Password Changes Successfuly!')
                    messages.success(request, "Password changed successfully")
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, "Please Select an Strong Password")
            except Exception as e:
                print(e.__str__())
        return render(request, 'core/passwordChange.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')