#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stefan Sollander'
SITENAME = 'Matematiska Python'
SITESUBTITLE = u'En webbsida med lite resurser om matematisk programmering i Python.'
SITEURL = ''

#Theme specific code
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'
PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'ipynb.markup']
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
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
