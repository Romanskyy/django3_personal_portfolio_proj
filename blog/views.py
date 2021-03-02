# imported function get_object_or_404() grab one object or show 404(no path)
from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def all_blogs(request):
    '''
    with this way you get all notes, all objects, in the blog

    blogs = Blog.objects.all()
    '''
    '''
    with comented next line of code you can get only last time
    notes inside the blog and sliced to last 3 ones
    '''
    # blogs = Blog.objects.order_by('-date')[:3]
    #  (-date) could change the blok or  the data
    blogs = Blog.objects.order_by('-date')

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    '''
      pk here is for database, means primary key
      Blog in this case is class name
    '''
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
