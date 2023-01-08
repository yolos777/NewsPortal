from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Post
from .filters import PostFilter
from .forms import ProductForm
from django.http import HttpRequest

class AllNews(ListView):
    model = Post
    ordering = ['-post_time']
    template_name = 'Content.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostList(ListView):
    model = Post
    ordering = ['-post_time']
    # queryset = Product.objects.order_by('-name')
    template_name = 'post_search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'Detailed_post.html'
    context_object_name = 'post'

class CategoryList(ListView):
    model = Category
    template_name = 'Categories.html'
    context_object_name = 'categories'
    ordering = 'name'


# Добавляем новое представление для создания товаров.
class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

    def form_valid(self, form):
        Post.author_name = self.request.user.author.id
        if HttpRequest('http://127.0.0.1:8000/news/'):
            self.news_or_article = 'новость'
        elif HttpRequest('http://127.0.0.1:8000/article/'):
            self.news_or_article = 'статья'

        return super().form_valid(form)
