#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stefan Sollander'
SITENAME = 'Matematiska Python'
SITESUBTITLE = u'En webbsida med lite resurser om matematisk programmering i Python.'
SITEURL = ''

#Theme specific code
THEME = 'pelican-themes/alchemy/alchemy'
#THEME = 'pelican-themes/Responsive-Pelican'


PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'ipynb.markup']
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SHOW_ARTICLE_CATEGORY = True

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'sv'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_PAGES_ON_MENU = False
