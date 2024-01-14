from . models import Blog
from user.models import M_User
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Function to Display the Home Page of the blog application, Here all the Available blogs will be shown in Descending manner
def BlogHome(request : HttpRequest) -> HttpResponse:
    '''
        The Function will Display all the Available Blogs in the Blog Model `objects.all()`.
        There should be Pagination while displaying the blogs!.
    '''
    Blog_list = Blog.objects.all().order_by('id') 
    paginator = Paginator(Blog_list, 5)
    page = request.GET.get('page', 1)
    print('This is Ok')
    blogs = None
    try:
        blogs = paginator.page(page)
        print('No Error in Blog')
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    print(Blog)
    return render(request, 'blog/blogHome.html', {'blogs' : blogs})

# Function to Display One Specific Blog Selected To Read
def OneBlog(request : HttpRequest, slug : str) -> HttpResponse:
    '''
        Function to Display a Specific Blog.
        Need to Make sure the Blog Title is shown in the URL (Slug Format).
    '''
    try:
        blog = Blog.objects.filter(slug=slug).first()
        return render(request, 'blog/oneBlog.html', {'blog' : blog, 'save_blog' : True})
    except Exception as e:
        print(e.__str__())
        return HttpResponseRedirect('/')

# Save Blog
def SaveBlog(request : HttpRequest, slug : str) -> HttpResponse:
    '''
        First Authenticate the User and is yes, then add the blog object of the saved_blogs field.
        And Redirect the User to the page where the user was!.
    '''
    id = request.user.id
    try:
        user = M_User.objects.filter(id=id)
        if user:
            blog = Blog.objects.filter(slug=slug).first()
            user.saved_blogs.append(blog)
            return
        return HttpResponseRedirect('/')
    except Exception as e:
        print(e.__str__())
        return HttpResponseRedirect('/blog/')