from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Function-based home view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# Class-based home view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # Naming convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post
    

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})



