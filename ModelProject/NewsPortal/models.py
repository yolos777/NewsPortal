from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

article = 'статья'
news = 'новость'

TYPE = [(article, 'статейка'), (news, 'новостейка')]


class Author(models.Model):
    author_name = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
       pass


class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    news_or_article = models.CharField(max_length = 50, choices = TYPE, default = article)
    post_time = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField(Category, through = 'PostCategory')
    headline = models.CharField(max_length = 255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.headline} \n {self.text}'


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.headline}. \n {self.text[0:125]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return self.comment

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()