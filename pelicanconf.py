#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bobe Kryant'
SITENAME = "Bobe's Thoughts"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('NBA Subreddit', 'http://reddit.com/r/nba'),
         ('NBA Stats', 'http://www.basketball-reference.com'),
         ('UFC Stats', 'http://www.ufcstats.com/statistics/events/completed'),
         ('My Github', 'https://github.com/bobekryant'),
		)

# Social widget
SOCIAL = (('Email', 'mailto:bobekryant33824'),)

# MARKUP = ('md', 'ipynb')
# MARKUP = ('md')
DEFAULT_PAGINATION = 10
THEME = 'elegant'
# THEME = 'notmyidea'
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['render_math']
STATIC_PATHS = ['images','static']
FAVICON = 'img/favicon.ico'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True