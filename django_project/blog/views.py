from django.shortcuts import render
from .models import Post

posts = [
    {
        'author':'Dan Kelly',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'August 27, 2021'
    },
    {
        'author':'Jane Does',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'August 28, 2021'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

