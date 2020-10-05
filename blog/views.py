from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# managing individual blog pages
class BlogDetailView(DetailView):
    # this is the database we are working on
    model = Post
    template_name = 'post_detail.html'

# A Class to add new post
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

# A class to edit blog post
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']