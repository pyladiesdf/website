from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from pathlib import Path
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
