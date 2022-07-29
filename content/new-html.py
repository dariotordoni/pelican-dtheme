import sys, os
from datetime import datetime

TEMPLATE = """
<html>
    <head>
        <title>{title}</title>
        <meta name="language" content="{lang}" />
        <meta name="summary" content="" />
        <meta name="seo_desc" content="" />
        <!-- <meta name="tags" content="" /> -->
        <meta name="alt" content="" />
        <meta name="hreflang_{lang2}" content="" />
        <meta name="hreflang_{lang}" content="/{slug}/" />
        <meta name="authors" content="Dario Tordoni" />
        <meta name="category" content="{category}" />
        <meta name="date" content="{year}-{month}-{day} {hour}:{minute:02d}" />
        <meta name="slug" content="{slug}" />
        <meta name="url" content="blog/{slug}/" />
        <meta name="cover_jpg" content="/theme/img/art-{slug}/copertina.jpg" />
        <meta name="cover_webp" content="/theme/img/art-{slug}/copertina.webp" />
        <meta name="cover_d1_jpg" content="/theme/img/art-{slug}/copertinaX1.jpg" />
        <meta name="cover_d1_webp" content="/theme/img/art-{slug}/copertinaX1.webp" />
        <meta name="cover_d2_jpg" content="/theme/img/art-{slug}/copertinaX2.jpg" />
        <meta name="cover_d2_webp" content="/theme/img/art-{slug}/copertinaX2.webp" />
        <meta name="cover1x1" content="/theme/img/art-{slug}/copertina_1x1.jpg" />
        <meta name="cover4x3" content="/theme/img/art-{slug}/copertina_4x3.jpg" />
        <meta name="cover16x9" content="/theme/img/art-{slug}/copertina_16x9.jpg" />
        <meta name="thumb_jpg" content="/theme/img/art-{slug}/thumb.jpg" />
        <meta name="thumb_webp" content="/theme/img/art-{slug}/thumb.webp" />
        <meta name="cat_webp" content="/theme/img/cat/{category}.webp" />
        <meta name="cat_jpg" content="/theme/img/cat/{category}.jpg" />
        # <meta name="status" content="draft" />
    </head>
    <body>
    </body>
</html>
"""

def make_entry(lang, title, category):
    if lang == "it":
        lang2 = "en"
    else:
        lang2 = "it"
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "{}_{:0>2}_{:0>2}_{}.html".format(
        today.year, today.month, today.day, slug)
    title = " ".join(title.split("-"))
    t = TEMPLATE.strip().format(title=title,
                                lang=lang,
                                lang2=lang2,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug,
                                category=category,)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)
    os.getcwd()
    os.mkdir("art-" + slug)
    os.chdir("../theme/dt/static/img")
    os.mkdir("art-" + slug)
    print("Folder created")

if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print ("Title or category are missing")
