from django import forms
from .models import Post, PostCategory, Category


class ProductForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
           'headline',
           'text',
           'categories',
        ]


