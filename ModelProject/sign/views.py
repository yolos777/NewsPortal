from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from NewsPortal.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/posts/'

@login_required
def upgrade_me(request):
    user = request.user
    if not Author.objects.filter(author_name=user).exists():
        Author.objects.create(author_name=user)

    return redirect('/posts/')




# @login_required
# def upgrade_me(request):
#     user = request.user
#     premium_group = Group.objects.get(name='authors')
#     if not request.user.groups.filter(name='authors').exists():
#         premium_group.user_set.add(user)
#
#     return redirect('/posts/')


