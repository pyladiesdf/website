from django.urls import path

from blog.views import Home, ListLadies

app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='about'),
    path('ladies/', ListLadies.as_view(), name='ladies'),
    path('material', Home.as_view(), name='material'),
    path('blog/', Home.as_view(), name='blog'),
]
