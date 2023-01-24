from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'headline')


admin.site.register(Author)
admin.site.register(Category)
#admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
