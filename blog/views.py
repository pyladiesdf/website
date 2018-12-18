from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Article

from pathlib import Path
import yaml
import re


class Home(TemplateView):
    template_name = "blog/index.html"


class ListLadies(ListView):
    template_name = 'blog/ladies.html'
    context_object_name = 'ladies'

    def get_context_data(self, **kwargs):
        context = super(ListLadies, self).get_context_data()

        context['medias'] = ['facebook', 'twitter', 'github']

        return context

    def get_queryset(self):
        with open(f'{Path(__file__).parents[0]}/content/ladies.yml', 'rb') as stream:
            try:
                ladies = yaml.load(stream)
            except yaml.YAMLError as exc:
                ladies = []
        return ladies


class ListMaterials(ListView):
    template_name = 'blog/materials.html'
    context_object_name = 'materials'

    def get_queryset(self):
        with open(f'{Path(__file__).parents[0]}/content/materials.yml', 'rb') as stream:
            try:
                materials = yaml.load(stream)
            except yaml.YAMLError as exc:
                materials = []
        return materials


class ListArticles(ListView):
    template_name = "blog/articles.html"
    context_object_name = "articles"
    model = Article

    def get_queryset(self):
        articles = super().get_queryset()
        print(articles[0])
        return articles

class ShowArticle(TemplateView):
    template_name = "blog/article.html"
    model = Article
    
    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data()
        slug = self.kwargs['slug']
        article = Article.objects.get(slug=slug)
        context['article'] = article
        return context
    
"""
def parse_article(html):
    div = html.split('<p>')
    attrs = div[1].replace('</p>', '').replace('\n', '').split('<br>')
    attr_dict = {}
    for attr in attrs:
        key, value = attr.split(': ')
        attr_dict[key] = value
    content = "<p>" + "<p>".join(div[2:])
    ctr = 0
    img_static = static('blog/img/')
    len_img_static = len(img_static)
    for m in re.finditer('<img src="', content):
        content = f'{content[:m.end()+ctr]}{img_static}{content[m.end()+ctr:]}'
        ctr += len_img_static
    attr_dict['content'] = content
    return attr_dict
"""