from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, CategoryList, PostDetail


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detailed'),
   path('categories/', CategoryList.as_view()),
]