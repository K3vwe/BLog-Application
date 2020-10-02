from django.shortcuts import render
from django.views.generic import ListView, DetailView
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