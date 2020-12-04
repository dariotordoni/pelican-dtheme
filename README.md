# pelican-dtheme

## Pelicanconf

### General section
```bash
AUTHOR = u'' # author name
SITENAME = u'' # sitename
SITEURL = '' # site url https://www.example.it
SITEDESCRIPTION = "" # meta description
BLOGNAME = u''
CSS_PATH = 'css' # legacy code, think about removing
IMG = "theme/img"
IMAGES_PATH = 'theme'
THEME = 'theme/dtheme'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'it'
TWITTERNAME = "" #twitter user name @example
PATH = 'content'
STATIC_PATHS = ['extra']
MENUITEMS = (('BLOG', '/blog/'),('ABOUT', '/chi-sono/'),) # the template is made for a two menu items, blog and about page. In this way I can manage the menu without using a hamburger menu and without using a javascript. Also, I don't need more than two menu items right one.

EXTRA_PATH_METADATA = { # use extra_path_metadata for static file needed in the root path, examples:
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/sw.js': {'path': 'sw.js'},
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/cookie_policy.pdf': {'path': 'cookie_policy.pdf'},
    'extra/privacy_policy.pdf': {'path': 'privacy_policy.pdf'},
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }
```
### Tracking section
Google tag manager only works if the variable GTM in publishconf.py it's true
```bash
GTM_HEAD = """ """ # Google tag manager script for the header section
GTM_BODY = """ """ # Google tag manager script for the body section
```
```bash
TRACKING = """ """ # I use this section to install custom tracking service like Google Analytics or other tools (fathom, plausible, goat analytics etc)
```
### Schema structured data section
Added up to four schema company. Use as much as you need
```bash
SCHEMA_JOB = "" # your job title
SCHEMA_PERSONAL_DESCRIPTION = "" # your personal description
SCHEMA_COMPANY = "" # company name
SCHEMA_COMPANY_LINK = "" # company url
SCHEMA_COMPANY_2 = ""
SCHEMA_COMPANY_LINK_2 = ""
SCHEMA_COMPANY_3 = ""
SCHEMA_COMPANY_LINK_3 = ""
SCHEMA_COMPANY_4 = ""
SCHEMA_COMPANY_LINK_4 = ""
```
### Various
```bash
# settings for XML feeds
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 10
RSS_FEED_SUMMARY_ONLY = True
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# settings for direct templating and pagination
DIRECT_TEMPLATES = ['home','error','blog_index','sitemap']
DEFAULT_PAGINATION = False
PAGINATED_TEMPLATES = {'blog_index': 5, 'tag': 5, 'category': 5, 'author':None}
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# settings for URLs configurations
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

# used in home, as links for my google certifications. 
GA_CERT = ''
GADS_DISPLAY_CERT = ''
GADS_SEARCH_CERT = ''

AUTHORS = {
    '[author name here]': { # put the name of the author. I made this template as a single author blog, so this is your name
        'short_description': """""", # used for the author info card inside at the bottom of the articles
        'description': """ """, # used inside the about page, immediately below the authore picture
        'long_description': """ """, #this is the long description placed inside the author about page
        'url': '/chi-sono/',
        'image_jpg': '/theme/img/autore/your-name.jpg',
        'image_webp': '/theme/img/autore/your-name.webp',
        'image_schema': '/theme/img/autore/your-name.jpg',
        'links': (('email', 'mailto:example@mail.com'),
                  ('linkedin', ''),
                  ('twitter', ''),
                  ('RSS', '/feeds/all.rss.xml'),)
    }
}
```
### Categories
```bash
# here you can set you categories. Putting new items inside the dictionary will create new categories pages. Categories can also be projects, they act the same way as blog listing about a single topic, it is just a way to see them.
CATEGORIES = {
    '': { # category name #1
        'description': "", # description of the category, used both for meta description and as a category main description, if no "project_description" is defined
    },
    '': { # category name #2
        'description': '',
        'logo_jpg': '/theme/img/cat/name.jpg', # "name" must be the name of the category
        'logo_webp': '/theme/img/cat/name.webp', # "name" must be the name of the category
        'project_info': True, # if True the category page will have several information at the bottom of the category name
        'project_description':'', # longer description of the category/project. If present, will replace the simpler "description"
        'project_tool':'', # tool used for the project management
        'project_lang': '', # lang used for the project
        'project_version': '', # project version
        'project_links': '', link to the project website
        'project_author': '' @ author of the project
    }
}

DISPLAY_CATEGORIES_ON_MENU = None
DISPLAY_PAGES_ON_MENU = None
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
# AUTORELOAD_IGNORE_CACHE = True

PLUGIN_PATHS = ['plugin']
PLUGINS = ['readtime', 'sitemap', 'cover_resizer', 'neighbors', 'pelican-toc'] # theese plugins are needed for the template to corret working. No tested without them
```

### Plugin settings
```bash
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
    'exclude': ['tag/', 'category/']
}

TOC = {
    'TOC_INCLUDE_TITLE': 'false',     # If 'true' include title in toc
}
```
