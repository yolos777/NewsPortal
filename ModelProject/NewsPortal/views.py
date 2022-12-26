from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment


class PostList(ListView):
    model = Post
    ordering = ['-post_time']
    # queryset = Product.objects.order_by('-name')
    template_name = 'Content.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'Detailed_post.html'
    context_object_name = 'post'

class CategoryList(ListView):
    model = Category
    template_name = 'Categories.html'
    context_object_name = 'categories'
    ordering = 'name'


