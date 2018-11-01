from django.urls import path

from blog.views import Home, ListLadies, ListMaterials, ListArticles, ShowArticle

app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='about'),
    path('ladies/', ListLadies.as_view(), name='ladies'),
    path('materials/', ListMaterials.as_view(), name='material'),
    path('blog/', ListArticles.as_view(), name='blog'),
    path('blog/article/<slug:slug>/', ShowArticle.as_view(), name='article'),
]
