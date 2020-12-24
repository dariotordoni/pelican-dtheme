#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#################
# GENERAL SECTION
#################
AUTHOR = u''
SITENAME = u''
SITEURL = ''
SITEDESCRIPTION = ""
BLOGNAME = u''
CSS_PATH = 'css'
IMG = "theme/img"
IMAGES_PATH = 'theme'
THEME = 'theme/dtheme'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'it'
TWITTERNAME = ""
PATH = 'content'
STATIC_PATHS = ['extra']
MENUITEMS = (('BLOG', '/blog/'),('ABOUT', '/chi-sono/'),)

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/sw.js': {'path': 'sw.js'},
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }

#################
# TRACKING SECTION
#################
GTM_HEAD = """"""
GTM_BODY = """"""
TRACKING = """"""

#################
# SCHEMA STRUCTURED DATA SECTION
#################
SCHEMA_WORKFOR = {
    "": {
        ""
        }
}
SCHEMA_ALUMNIOF = {
    "": {
        ""
        }
}
SCHEMA_JOB = ""
SCHEMA_PERSONAL_DESCRIPTION = ""

SCHEMA_LINK_SAMEAS = {
    ('', ''),
    ('', '')
}

#################
# VARIOUS
#################
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 10
RSS_FEED_SUMMARY_ONLY = True
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['home','error','blog_index','sitemap','utmbuilder']
DEFAULT_PAGINATION = False
PAGINATED_TEMPLATES = {'blog_index': 5, 'tag': 5, 'category': 5, 'author':None}
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

AUTHOR_URL = 'chi-sono/'
AUTHOR_SAVE_AS = 'chi-sono/index.html'

HOME_URL = 'index.html'
HOME_SAVE_AS = 'index.html'

BLOG_INDEX_URL = 'blog/'
BLOG_INDEX_SAVE_AS = 'blog/index.html'

CATEGORY_URL = 'cat/{slug}/'
CATEGORY_SAVE_AS = 'cat/{slug}/index.html'

SITEMAP_URL = 'mappa-sito/'
SITEMAP_SAVE_AS = 'mappa-sito/index.html'

UTMBUILDER_URL = 'utmbuilder/'
UTMBUILDER_SAVE_AS = 'utmbuilder/index.html'

ERROR_URL = '404/'
ERROR_SAVE_AS = '404/index.html'

CERTIFICATION = True # if False it hides the certification section
CERTIFICATIONS = {
    '': {
        'url': '',
        'title': '',
        'img': '',
        'alt_tag': ''
    }
}

AUTHORS = {
    '': {
        'short_description': """""",
        'description': """""",
        'long_description': """""",
        'work_description':"""""",
        'url': '/chi-sono/',
        'image_jpg': '/theme/img/autore/***.jpg', # just add the file name
        'image_webp': '/theme/img/autore/***.webp', # just add the file name
        'links': (('email', 'mailto:'),
                  ('', ''),
                  ('', ''),
                  ('', ''),)
    }
}

#################
# CATEGORIES SECTION
#################
CATEGORIES = {
    'blog': {
        'description': ".",
    },
    '': {
        'description': '',
        'logo_jpg': '/theme/img/cat/***.jpg', # just add the file name
        'logo_webp': '/theme/img/cat/***.webp', # just add the file name
        'project_info': True,
        'project_description':'',
        'project_tool':'',
        'project_lang': '',
        'project_version': '',
        'project_links': '',
        'project_author': ''
    }
}

DISPLAY_CATEGORIES_ON_MENU = None
DISPLAY_PAGES_ON_MENU = None
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

#################
# PROJECTS SECTION INSIDE THE AUTHOR PAGE
#################
PROJECTS = {
    '': {
        'image_jpg':'',
        'image_webp':'',
        'alt_tag':'',
        'description':""""""
    }
}

#################
# PLUGIN SETTINGS
#################
PLUGIN_PATHS = ['plugin']
PLUGINS = ['readtime', 'sitemap', 'cover_resizer', 'neighbors', 'pelican-toc', 'minification']

MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "weekly",
        "pages": "monthly"
    },
    'exclude': ['tag/', 'category/', '404/']
}

TOC = {
    'TOC_INCLUDE_TITLE': 'false'
}
