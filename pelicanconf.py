#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Singpro'
SITENAME = u'Singpro'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = u'en'


#ARCHIVES_SAVE_AS = 'blog/index.html'

#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/{number}/','{base_name}/{number}/index.html'),
#)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None #'feeds/all.atom.xml'
FEED_ALL_RSS = None #'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None #'feeds/%s.rss.xml'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# static
STATIC_PATHS = ['static', 'downloads']
#THEME = '/u/49/tewodrod/unix/spike/pelican-bootstrap3-lovers'
THEME = 'notmyidea'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/pages/home.html'),
    ('About', '/pages/about.html'),
    ('Contact', '/pages/contact.html'),
    ('Research', '/category/research.html')
    )
