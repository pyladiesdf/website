from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from blog.views import Home, ListLadies, ListMaterials, ListArticles, ShowArticle

app_name = 'blog'

urlpatterns = [
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', Home.as_view(), name='about'),
    path('ladies/', ListLadies.as_view(), name='ladies'),
    path('materials/', ListMaterials.as_view(), name='material'),
    path('blog/', ListArticles.as_view(), name='blog'),
    path('blog/article/<slug:slug>/', ShowArticle.as_view(), name='article'),
]