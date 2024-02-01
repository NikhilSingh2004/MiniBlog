from blog.models import Blog
from user.models import M_User
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Function to Display the Home Page of the Author
@login_required
def AuthorHome(request : HttpRequest) -> HttpResponse:
    '''
        First Check if the User is_Author, if True let the user Access the Home Page of the AuthHome,
        Else HttpResponseRedirect the User to Be_Author Page!.

        If Already a Author, then fetch all the Blog Model Row that have the Author's User ID and Display them, with Pagination
    '''
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
        return render(request, 'author/authHome.html', context)
    messages.warning(request, "You Might Have to Become an Author First!")
    return HttpResponseRedirect('/user/')

@login_required
def BeAuthor(request : HttpRequest) -> HttpResponse:
    '''
        First Check if the User is authenticated!.
        If the user is already an author -> Redirect to Author Home Page
        If not then set the request user's is_author property to True (Becomes Author)
    '''
    if request.user.is_author:
        return HttpResponseRedirect('/author/')
    try:
        user = M_User.objects.filter(id=request.user.id, is_deleted = False).first()
        if user:
            user.is_author = True
            user.save()
            messages.success(request, f"Welcome, {user.username}")
            return HttpResponseRedirect('/author/')
        messages.error(request, "User Not Found!")
    except Exception as e:
        print(e.__str__())
        return HttpResponseRedirect('/')
    
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