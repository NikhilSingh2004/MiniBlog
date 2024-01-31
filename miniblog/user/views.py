from .models import M_User
from blog.models import Blog
from .forms import EditProfileForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# User Home
def UserHome(request : HttpRequest) -> HttpResponse:
    '''
        First Check is the request.user is Authenticated, if yes the render the User Home Page!.
        The User Home Page Should Consist of all the Blog's the User have saved
    '''
    if request.user.is_authenticated:
        
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

        user = None
        try:
            user = request.user.first_name + " " + request.user.last_name
        except Exception as e:
            pass

        notAuthor = True
        if request.user.is_author:
            notAuthor = False

        context ={
            'user_name' : user,
            'loged_in' : True,
            'blogs' : blogs,
            'notAuthor' : notAuthor
        }
        return render(request, 'user/userHome.html', context)
    context ={
        'sign_log' : True
    }
    return HttpResponseRedirect('/login/')

# Edit Profile Function
@login_required
def EditUser(request: HttpRequest, id: int) -> HttpResponse:
    '''
    Check for Authentication, if yes proceed.
    If the request is GET -> Initialize the Edit Form with User Object and Render
    If the request is POST -> Load the Data & Validate the Input Data, is all good then Save
    '''
    user_instance = get_object_or_404(M_User, id=id, is_deleted=False)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Edited Successfully")
            return HttpResponseRedirect('/user/')
        messages.error(request, "Something Went Wrong")
        return render(request, 'user/editProfile.html', {'form': form})
    form = EditProfileForm(instance=user_instance)
    return render(request, 'user/editProfile.html', {'form': form})

# Delete User Softly
@login_required
def DeleteUser(request :  HttpRequest, id : int) -> HttpResponse:
    '''
        Function to delete the user. First Make sure the user is authenticated 
        Do not do hard delete! Make a soft delete
    '''
    user = get_object_or_404(M_User, id=id, is_deleted=False)
    if user:
        user.is_deleted = True
        logout(user)
        messages.danger(request, "Profile Deleted Successfuly")
        return HttpResponseRedirect("/")
    messages.error(request, "User Not Found!")
    return HttpResponseRedirect('/user/')