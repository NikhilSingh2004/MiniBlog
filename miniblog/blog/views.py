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
    blogs = None
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    if request.user.is_authenticated:
        return render(request, 'blog/blogHome.html', {'blogs' : blogs, 'loged_in':True})
    return render(request, 'blog/blogHome.html', {'blogs' : blogs, 'sign_log':True})

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
    if request.user.is_authenticated:
        id = request.user.id
        print(id)
        try:
            user = M_User.objects.filter(id=id).first()
            if user:
                print(user)
                print(user.saved_blogs)
                blog = Blog.objects.filter(slug=slug).first()
                print(blog.title)
                user.saved_blogs.add(blog)
                print(user.saved_blogs)
                return HttpResponseRedirect(f'/blog/{slug}')
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e.__str__())
            return HttpResponseRedirect('/blog/')
    else:
        return HttpResponseRedirect('/login/')