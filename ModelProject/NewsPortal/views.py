from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment


class ContentList(ListView):
    model = Post
    ordering = 'categories'
    # queryset = Product.objects.order_by('-name')
    template_name = 'Content.html'
    context_object_name = 'allnews'

class ArticlesDetail(DetailView):
    model = Post
    template_name = 'Articles.html'
    context_object_name = 'article'
