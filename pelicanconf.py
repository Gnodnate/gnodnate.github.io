#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gondnat'
SITENAME = 'Hardcode Today'

THEME = 'themes/alchemy'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME speical
SITEIMAGE = '/theme/images/avatar.jpg width=168 height=168'

DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
              'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
ICONS = (
    ('twitter', 'https://twitter.com/gondnat'),
    ('github', 'https://github.com/gondnat'),
)

PYGMENTS_STYLE = 'vs'

HIDE_AUTHORS = True
RFG_FAVICONS = True