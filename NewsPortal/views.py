from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .filters import PostFilter
from .forms import ProductForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .tasks import hello, printer
from django.http import HttpResponse
from django.core.cache import cache


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

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj

class CategoryList(ListView):
    model = Category
    template_name = 'Categories.html'
    context_object_name = 'categories'
    ordering = 'name'

class PostCategory(ListView):
    model = Post
    template_name = 'test.html'
    context_object_name = 'cats'
    ordering = ['-post_time']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(categories=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Post.objects.filter(categories=self.kwargs['pk'])
        return context


class PostCreate(CreateView):
    form_class = ProductForm
    model = Post
    template_name = 'post_edit.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = Author.objects.get(author_name=self.request.user)
        if 'news' in self.request.path:
            self.object.news_or_article = news

        self.object.save()
        ...
        return super().form_valid(form)

        html_content = render_to_string('Subscribers_notify.html')

        msg = EmailMultiAlternatives(subject=f'{Post.headline}', body=Post.text , from_email='Leemur1504@yandex.ru', to=[User.email])
        msg.attach_alternative(html_content, "Subscribers_notify")

        msg.send()


class PostUpdate(UpdateView, LoginRequiredMixin, TemplateView):
    form_class = ProductForm
    model = Post
    template_name = 'post_edit.html'


class AddPost(PermissionRequiredMixin, PostCreate):
    permission_required = ('NewsPortal.add_post',
                           'NewsPortal.delete_post',
                           'NewsPortal.change_post')


class IndexView(View):
    def get(self, request):
        printer.apply_async([10], countdown = 5)
        hello.delay()  #delay - это метод для вызова задач
        return HttpResponse('Hello!')

@login_required
def subscribe(request, pk):
    user = request.user
    c = Category.objects.get(id=pk)

    if not c.subscribers.filter(id=user.id).exists():
        c.subscribers.add(user)
        html = ...
    return redirect('posts/subscribe')

@login_required
def unsubscribe(request, pk):
    user = request.user
    c = Category.objects.get(id=pk)

    if c.subscribers.filter(id=user.id).exists():
        c.subscribers.remove(user)
    return redirect('')