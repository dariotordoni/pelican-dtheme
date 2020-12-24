#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False
MENUITEMS = (('BLOG', ''),('ABOUT', ''),)

# con questa variabile indico al sistema di leggere solo i contenuti che sono stati modificati.
# Pelican salva in cache gli hash dei file e li confronta
# LOAD_CONTENT_CACHE = True

# confronta il tempo della modifica
# CHECK_MODIFIED_METHOD = 'mtime'

# confronta l'hash del documento; è più lento
CHECK_MODIFIED_METHOD = 'md5'

# salva le informazioni del file in cache in modo che possano essere lette al prossimo uso
# CACHE_CONTENT = True

# --------------------------------------------------------------------------------
# usa questa variabile per indicare le pagine per le quali vuoi generare l'HTML.
# In questo modo avrai la data modificata solo per quelle
# --
# --
# WRITE_SELECTED = []
# --
# --
# --------------------------------------------------------------------------------


#FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

GTM = False
