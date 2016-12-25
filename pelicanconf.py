#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yanwar Solahudin'
SITENAME = '@yanwarsolah'
SITEURL = 'https://yanwarsolah.github.io'


# PATH = 'content'
# STATIC_PATHS = ['blog', 'downloads']
# ARTICLE_PATHS = ['blog']

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'id'
THEME = 'pelican-blue'
SIDEBAR_DIGEST = 'Programmer and Web Developer'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'yanwarsolah'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MENUITEMS = (('Blog', SITEURL),)
DISQUS_SITENAME = "yanwarsolah"

# Blogroll
# LINKS = ((),)

# Social widget
SOCIAL = (
			('Facebook', 'https://www.facebook.com/yanwarsolah'),
			('Github', 'https://github.com/yanwarsolah/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
