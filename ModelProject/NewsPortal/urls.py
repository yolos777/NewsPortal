from django.urls import path
from .views import PostList, CategoryList, PostDetail, PostCreate


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detailed'),
   path('categories/', CategoryList.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
]