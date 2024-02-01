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
        if request.user.is_author:
            Blog_list = Blog.objects.filter(author=request.user.id)
            paginator = Paginator(Blog_list, 5)
            page = request.GET.get('page', 1)
            blogs = None
            try:
                blogs = paginator.page(page)
            except PageNotAnInteger:
                blogs = paginator.page(1)
            except EmptyPage:
                blogs = paginator.page(paginator.num_pages)

            context = {
                'blogs' : blogs,
                'loged_in' : True,
                'notAuthor' : False,
                'user' : request.user.first_name + " " + request.user.last_name,
            }
            return render(request, 'user/userHome.html', context)

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
            'user' : user,
            'loged_in' : True,
            'blogs' : blogs,
            'notAuthor' : notAuthor
        }
        return render(request, 'user/userHome.html', context)
    context ={
        'sign_log' : True
    }
    return HttpResponseRedirect('/login/')

# Function to Make the user an Author
@login_required
def BeAuthor(request : HttpRequest) -> HttpResponse:
    '''
        First Check if the User is authenticated!.
        If the user is already an author -> Redirect to Author Home Page
        If not then set the request user's is_author property to True (Becomes Author)
    '''
    if request.user.is_author:
        return HttpResponseRedirect('/user/')
    try:
        user = M_User.objects.filter(id=request.user.id, is_deleted = False).first()
        if user:
            user.is_author = True
            user.save()
            messages.success(request, f"Welcome, {user.username}")
            return HttpResponseRedirect('/user/')
        messages.error(request, "User Not Found!")
        return HttpResponseRedirect('/')
    except Exception as e:
        print(e.__str__())
        return HttpResponseRedirect('/')

# Function to delete Author Account
@login_required
def DeleteAuthor(request : HttpRequest) -> HttpResponse:
    if request.user.is_author:
        try:
            user = M_User.objects.get(id=request.user.id, is_deleted=False)
            if user:
                user.is_author = False
                user.save()
                messages.warning(request, "Sad to see lose an Author")
                return HttpResponseRedirect('/user/')
            messages.error(request, "Something Went Wrong!")
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e.__str__())
            messages.error(request, "User Not Found")
            return HttpResponseRedirect('/user/')
    messages.error(request, "Not An Author Account")
    return HttpResponseRedirect('/user/')

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