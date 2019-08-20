#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.hardcode.today'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

FORCE_HTTPS = "<script type=\"text/javascript\">\
  var targetProtocol = \"https:\";\
  if (window.location.protocol != targetProtocol)\
    window.location.href = targetProtocol +\
      window.location.href.substring(window.location.protocol.length);\
</script>"

# Following items are often useful when publishing

DISQUS_SITENAME = "http-gnodnate-github-io-gnod-doc"
GOOGLE_ANALYTICS = "UA-142996929-1"

STATIC_PATHS = ['images']