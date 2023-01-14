from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Post
from .filters import PostFilter
from .forms import ProductForm
from django.contrib.auth.mixins import PermissionRequiredMixin
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



class PostCreate(CreateView):
    form_class = ProductForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, request):
        self.object = ProductForm.save()
        return super().form_valid(ProductForm)

class PostUpdate(UpdateView, LoginRequiredMixin, TemplateView):
    form_class = ProductForm
    model = Post
    template_name = 'post_edit.html'


class AddPost(PermissionRequiredMixin, PostCreate):
    permission_required = ('NewsPortal.add_post',
                           'NewsPortal.delete_post',
                           'NewsPortal.change_post')

