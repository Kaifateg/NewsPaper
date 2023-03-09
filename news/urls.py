from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('news/', cache_page(60)(PostNews.as_view()), name='post_info'),
    path('news/<int:pk>', cache_page(300)(PostNW.as_view()), name='news_info'),
    path('news/search', PostFilters.as_view(), name='post_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('news/categories/<int:pk>', CategoryListViev.as_view(), name='category_info'),
    path('news/categories/<int:pk>/follow', follow, name='follow'),
]