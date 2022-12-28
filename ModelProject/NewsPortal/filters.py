from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter
from .models import Post, Category
from django import forms

class PostFilter(FilterSet):
    categories = ModelChoiceFilter(
        field_name='postcategory_category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='любая',
    )

    post_time = DateFilter(widget=forms.DateInput(attrs={'type':'date', 'value':'2022-12-28'}), lookup_expr='gt', label='Опубликовано после')
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='Заголовок')

    class Meta:
        model = Post
        fields = ['post_time', 'headline']