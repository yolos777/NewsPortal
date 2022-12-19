from django.urls import path
# Импортируем созданное нами представление
from .views import ContentList, ArticlesDetail


urlpatterns = [
   path('', ContentList.as_view()),
   path('<int:pk>', ArticlesDetail.as_view()),
]