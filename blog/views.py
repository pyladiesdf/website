from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from pathlib import Path
import mistune
import yaml


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
        with open(f'{Path(__file__).parents[0]}/content/ladies.yml', 'r') as stream:
            try:
                ladies = yaml.load(stream)
            except yaml.YAMLError as exc:
                ladies = []
        return ladies


class ListMaterials(ListView):
    template_name = 'blog/materials.html'
    context_object_name = 'materials'

    def get_queryset(self):
        with open(f'{Path(__file__).parents[0]}/content/materials.yml', 'r') as stream:
            try:
                materials = yaml.load(stream)
            except yaml.YAMLError as exc:
                materials = []
        return materials


class ListArticles(ListView):
    template_name = 'blog/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        local = Path(__file__).parents[0]
        articles_files = Path(f'{local}/content/articles/').glob('*')
        files = [article for article in articles_files if article.is_file()]
        articles = []
        for f in files:
            with open(f'{Path(__file__).parents[0]}/content/articles/{f.name}', 'r') as stream:
                renderer = mistune.Renderer(escape=True, hard_wrap=True)
                art = mistune.Markdown(renderer=renderer)
                articles.append(parse_article(art.render(stream.read()), f.name))
        return articles


class ShowArticle(TemplateView):
    template_name = "blog/article.html"

    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data()
        slug = self.kwargs['slug']
        with open(f'{Path(__file__).parents[0]}/content/articles/{slug}.md', 'r') as stream:
            renderer = mistune.Renderer(escape=True, hard_wrap=True)
            art = mistune.Markdown(renderer=renderer)
            article = parse_article(art.render(stream.read()), f'{slug}.md')
        context['article'] = article
        return context


def parse_article(html, filename):
    div = html.split('<p>')
    attrs = div[1].replace('</p>', '').replace('\n', '').split('<br>')
    attr_dict = {}
    for attr in attrs:
        key, value = attr.split(': ')
        attr_dict[key] = value
    content = "<p>".join(div[2:])
    attr_dict['content'] = content
    attr_dict['filename'] = filename[:-3]
    return attr_dict
