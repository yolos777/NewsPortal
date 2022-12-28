from django import forms
from .models import Post
# from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
   text = forms.CharField(min_length=20)

   class Meta:
       model = Post
       fields = [
           'author',
           'news_or_article',
           'headline',
           'text',
       ]

   # def clean(self):
   #     cleaned_data = super().clean()
   #     text = cleaned_data.get('text')
   #
   #     return cleaned_data