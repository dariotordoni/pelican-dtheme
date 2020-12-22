# pelican-dtheme

DTeheme is a theme developed for Pelican. The goal is to create a theme that allows people to generate a fast website, lightweight and attentive to the metrics of web vitals.
This is not a documentation, but it is the closest thing to documentation that I can do right now. I hope it will be useful.
[Here](https://www.dariotordoni.it) you can find my personal website where I use, at the time of writing, this theme.

Some plugins are needed in order for the theme to work:
* [readtime](https://github.com/getpelican/pelican-plugins/tree/master/readtime)
* [sitemap](https://github.com/getpelican/pelican-plugins/tree/master/sitemap)
* [cover_resizer]()
* [neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
* [pelican-toc](https://github.com/ingwinlu/pelican-toc) I just made some changes here, but haven't proposed them to its developer yet
* [minification](https://pypi.org/project/pelican-minification/) 

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
MENUITEMS = (('BLOG', '/blog/'),('ABOUT', '/chi-sono/'),) # the template is made for a two menu items, blog and about page. In this way I can manage the menu without using a hamburger menu and without using a javascript. Also, I don't need more than two menu items right one. At the moment there is a misconfiguration and this settings field is also in publishconf.py file, better to use the one in the publishconf.

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
I just give a one key example, but use as much keys as you need
```bash
SCHEMA_WORKFOR = {
    "your company name": {
        "company url"
        } # add comma and continue adding key/values if needed
}
SCHEMA_ALUMNIOF = {
    "education organization name": {
        "education organization url"
        } # add comma and continue adding key/values if needed
}
SCHEMA_JOB = "" # your job title
SCHEMA_PERSONAL_DESCRIPTION = "" # your personal description

SCHEMA_LINK_SAMEAS = {
    ('', ''), # name and link of your same as (ex. "linkedin", "https://linkedin.com/myprofile"). Add comma and continue adding key/values if needed
}
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

# used in about page, as links for my google certifications. 
CERTIFICATION = True # set False to not show any certifaction logo
GA_CERT = ''
GADS_DISPLAY_CERT = ''
GADS_SEARCH_CERT = ''

AUTHORS = {
    'author name here': { # put the name of the author. I made this template as a single author blog, so this is your name
        'short_description': """""", # used for the author info card inside at the bottom of the articles
        'description': """ """, # used inside the about page, immediately below the authore picture
        'long_description': """ """, #this is the long description placed inside the author about page
        'url': '/chi-sono/',
        'image_jpg': '/theme/img/autore/your-name.jpg', # used as author avatar
        'image_webp': '/theme/img/autore/your-name.webp', # used as author avatar
        'image_schema': '/theme/img/autore/your-name.jpg', # used for structured data
        'links': (('email', 'mailto:example@mail.com'),
                  ('linkedin', ''),
                  ('twitter', ''),
                  ('RSS', '/feeds/all.rss.xml'),)
    }
}
```
### Categories
```bash
# here you can set you categories. Putting new items inside the dictionary will create new categories pages. Categories can also talks about projects, they act the same way as blog listing about a single topic, it is just a way to see them.
CATEGORIES = {
    'blog': { # this is the main category, a kind of blog home. Give it the name you like, I call it "blog". 
        'description': "", # description of the blog, used both for meta description and as a category main description, if no "project_description" is defined
    },
    '': { # here you can specify a real category name
        'description': '',
        'logo_jpg': '/theme/img/cat/name.jpg', # "name" must be the name of the category
        'logo_webp': '/theme/img/cat/name.webp', # "name" must be the name of the category
        'project_info': True, # if True the category page will have several information at the bottom of the category name
        'project_description':'', # longer description of the category/project. If present, will replace the simpler "description"
        'project_tool':'', # tool used for the project management
        'project_lang': '', # lang used for the project
        'project_version': '', # project version
        'project_links': '', # link to the project website
        'project_author': '' # author of the project
    }
}

DISPLAY_CATEGORIES_ON_MENU = None
DISPLAY_PAGES_ON_MENU = None
RELATIVE_URLS = True # Uncomment following line if you want document-relative URLs when developing
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
```
### Project section
```bash
# Usefull for the author page. These information are used to create the project slider
PROJECTS = {
    '': { # here the name of the project
        'image_jpg':'', # just the name of the project main image, jpg file
        'image_webp':'', # just the name of the project main image, webp file
        'alt_tag':'', # alt tag for the project image inside the slider
        'description':"""""" # description of the project. It will appear under the slider image
    }
}
```
### Plugin settings
```bash
PLUGIN_PATHS = ['plugin']
PLUGINS = ['readtime', 'sitemap', 'cover_resizer', 'neighbors', 'pelican-toc', 'minification'] # theese plugins are needed for the template to corret working. No tested without them

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
    'exclude': ['tag/', 'category/']
}

TOC = {
    'TOC_INCLUDE_TITLE': 'false'
}
```



## Publishconf

### General
```bash
SITEURL = '' # website url
RELATIVE_URLS = False
MENUITEMS = (('BLOG', ''),('ABOUT', ''),) #this is the filed to use in order to set the menu items
#FEED_ALL_ATOM = 'feeds/all.atom.xml' commented by default
FEED_ALL_RSS = 'feeds/all.rss.xml'
DELETE_OUTPUT_DIRECTORY = True
GTM = False # set True if want to install Google tag manager
```



## PWA

### Manifest
```bash
{
    "manifest_version": 1,
    "version": "1.0.0",
    "short_name": "", # the name of your website here
    "name": "", # the name of your website here
    "description": "", # the description of your website here
    "icons": [
        {
        "src": "theme/img/pwa512.png",
        "sizes": "512x512",
        "type": "image/png"
        },
        {
        "src": "theme/img/maskable_icon.png",
        "sizes": "512x512",
        "type": "image/png",
        "purpose": "any maskable"
        },
        {
        "src": "theme/img/pwa144.png",
        "sizes": "144x144",
        "type": "image/png"
        }
    ],
    "start_url": "/?utm_source=pwa&utm_medium=app", 
    "lang": "it-IT",
    "background_color": "#353e47",
    "theme_color": "#353e47",
    "display": "standalone",
    "orientation": "portrait-primary"
    }
```

### Service worker
```bash
/*
 Copyright 2016 Google Inc. All Rights Reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */
// Names of the two caches used in this version of the service worker.
// Change to v2, etc. when you update any of the local resources, which will
// in turn trigger the install event again.
const PRECACHE = 'precache-v1';
const RUNTIME = 'runtime';

// A list of local resources we always want to be cached.
const PRECACHE_URLS = [
  'index.html',
  './', // Alias for index.html
  '/theme/css/main.css',
];

// The install handler takes care of precaching the resources we always need.
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(PRECACHE)
      .then(cache => cache.addAll(PRECACHE_URLS))
      .then(self.skipWaiting())
  );
});

// The activate handler takes care of cleaning up old caches.
self.addEventListener('activate', event => {
  const currentCaches = [PRECACHE, RUNTIME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return cacheNames.filter(cacheName => !currentCaches.includes(cacheName));
    }).then(cachesToDelete => {
      return Promise.all(cachesToDelete.map(cacheToDelete => {
        return caches.delete(cacheToDelete);
      }));
    }).then(() => self.clients.claim())
  );
});

// The fetch handler serves responses for same-origin resources from a cache.
// If no response is found, it populates the runtime cache with the response
// from the network before returning it to the page.
self.addEventListener('fetch', event => {
  // Skip cross-origin requests, like those for Google Analytics.
  if (event.request.url.startsWith(self.location.origin)) {
    event.respondWith(
      caches.match(event.request).then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse;
        }

        return caches.open(RUNTIME).then(cache => {
          return fetch(event.request).then(response => {
            // Put a copy of the response in the runtime cache.
            return cache.put(event.request, response.clone()).then(() => {
              return response;
            });
          });
        });
      })
    );
  }
});
```



## Filo to provide
```bash
author pics under "/static/img/autore" folder
cat pics under "/static/img/cat" folder
projects pics under "/static/img/progetti"
favicon under "/static/img/" folder
    favicon.ico
    favicon57.ico
    favicon72.ico
    favicon114.ico
    maskable_icon.png
    pwa144.png
    pwa512.png
```



## How create new content
I like writing content using html. I created the "new-html.py" file in order to facilitate myself creating new content. Run it in this way
```bash
python new-html.py slug-of-the-post category
ex.
python new-html.py hello-world-this-is-my-first-post coding
```
The script will create a new html file called as the slug provided. Inside the file, you will find several meta tags, some of them already filled
```bash
    <head>
        <title></title> # here there will be the slug too, change it with the title of the article (add stopwords..)
        <meta name="summary" content="" /> # add the summary used inside the blog listing pages
        <meta name="seo_desc" content="" /> # add meta description for google
        <meta name="date" content="" /> # automatic
        <meta name="tags" content="" /> # leave blank
        <meta name="category" content="" /> # automatic
        <meta name="slug" content="" /> # automatic
        <meta name="url" content="" /> # automatic
        <meta name="cover_jpg" content="" /> # automatic
        <meta name="cover_webp" content="" /> # automatic
        <meta name="cover_d1_jpg" content="" /> # automatic
        <meta name="cover_d1_webp" content="" /> # automatic
        <meta name="cover_d2_jpg" content="" /> # automatic
        <meta name="cover_d2_webp" content="" /> # automatic
        <meta name="cover1x1" content="" /> # automatic
        <meta name="cover4x3" content="" /> # automatic
        <meta name="cover16x9" content="" /> # automatic
        <meta name="thumb_jpg" content="" /> # automatic
        <meta name="thumb_webp" content="" /> # automatic
        <meta name="cat_webp" content="" /> # automatic
        <meta name="cat_jpg" content="" /> # automatic
        <meta name="alt" content="" /> # add tje alt tag for the hero image and the thumb of the article
        <meta name="authors" content="" /> # add your name. It must be the same setted inside AUTHORS dict on peliconf.py
    </head>
```
The script will also create two folder called as the slug provided:
* the first under "/content" where you will must put the main image of the article, used for hero images and thums
* the second under "/theme/static/img/" where will be placed all the adaptation of the main image (see the next section about the "cover_resizer" plugin). I also use this folder to put in images and/or video that I refer to inside the article.



## Custom plugin
I created a plugin called "cover_resizer", I consider it still in beta. Looping for all the content provided, it takes a jpg image and generates from it all the adaptation:
* webp
* thumbs
* different sizes (usefull for article rich snippet).

To make it works, you have to put the main image of an article under the "/content/your-article/ folder and name it "cover_raw.jpg".
During the output generation process, or starting the local server, this script will process the main image and create the adaptations. After that will rename the main image removing the "_raw" suffix
