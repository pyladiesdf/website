#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from collections import namedtuple

import os
import yaml

AUTHOR = u'Pyladies'
SITENAME = u'Pyladies DF'
SITEURL = 'http://localhost:{}'.format(os.getenv('PORT', '8000'))
TAGLINE = (u'Ninguém pode fazer você se sentir inferior'
           'sem o seu consentimento (Eleanor Roosevelt)')
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_BG = 'images/pyladiesdf.png'
SINCE = datetime.now().year
NOW = datetime.now().date()
SUMMARY_MAX_LENGTH = 30

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{}index.html'.format(ARTICLE_URL)

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Sitemap
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'
THEME = 'themes/default'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Sobre', '/about'),
    ('Ladies', '/ladies'),
    ('Materiais', '/materiais'),
    ('Blog', '/archives.html'),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/robots.txt',
                'extra/favicon.ico', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'}
}

# ANALYTICS
GOOGLE_ANALYTICS_UA = 'UA-58961512-1'

DISQUS_SITENAME = 'pyladiesdf'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Ladies, Locations, Events and Videos
with open('data/ladies.yml') as ladies:
    ladies_converted = yaml.load(ladies.read())
    LADIES = []
    for lady in ladies_converted:
        LADIES.append(
            namedtuple('Ladies', lady.keys())(**lady)
        )

with open('data/materials.yml') as materials:
    materials_readed = yaml.load(materials.read())
    MATERIALS = []
    for materials in materials_readed:
        MATERIALS.append(
            namedtuple('Materials', materials.keys())(**materials)
        )

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']
