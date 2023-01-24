from django.urls import path
from .views import PostList, PostDetail, AllNews, PostUpdate, PostCreate, IndexView, PostCategory, CategoryList
from .views import subscribe, unsubscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('search/', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view(), name = 'post_detailed'),
   path('categories/', CategoryList.as_view()),
   path('categories/<int:pk>/', PostCategory.as_view(), name = 'cats'),
   path('news/', PostCreate.as_view(), name='post_create'),
   path('articles/', PostCreate.as_view(), name='post_create'),
   path('', cache_page(60*5)(AllNews.as_view())),
   path('celery', IndexView.as_view()),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('subscribe/', subscribe, name='subscribe'),
   path('unsubscribe/', unsubscribe, name='unsubscribe')
]