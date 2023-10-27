AUTHOR = 'Rakibul Hasan'
SITENAME = 'Rakibul Hasan'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images','extras','pdfs']
EXTRA_PATH_METADATA = {
        'extras/favicon.ico': {'path': 'favicon.ico'},
}

# specify the custom theme directory
THEME = 'theme'

TIMEZONE = 'Australia/Perth'

DEFAULT_LANG = 'en-au'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('Google Scholar','https://scholar.google.com.au/citations?user=DuCQ8goAAAAJ&hl=en'),
        ('ORCiD','https://orcid.org/0000-0003-2565-5321'),
        ('ReserchGate','https://www.researchgate.net/profile/Md-Rakibul-Hasan-10'),
        ('Semantic Scholar', 'https://www.semanticscholar.org/author/2142425'),
        ('dblp','https://dblp.org/pid/122/5190-1.html'),
        ('Web of Science','https://www.webofscience.com/wos/author/record/AFK-8839-2022'),
        ('LinkedIn','https://www.linkedin.com/in/m-rakibul'),
        ('GitHub','https://github.com/hasan-rakibul'),
        ('Curtin University','https://staffportal.curtin.edu.au/staff/profile/view/rakibul-hasan-145a1046/'),
        ('BRAC University','https://www.bracu.ac.bd/about/people/md-rakibul-hasan'),
        ('e-mail','mailto:Rakibul.Hasan@curtin.edu.au'),
        )

LINKS_WIDGET_NAME = 'find me on'

# Social widget
# SOCIAL = (
#         ('e-mail','mailto:rakibul.hasan@`bracu.ac.bd'),
#         ('GitHub','https://github.com/mrh-rakib'),
#         ('LinkedIn','https://www.linkedin.com/in/rakibul-eeekuet/'),
#         ('ORCiD','https://orcid.org/0000-0003-2565-5321'),
#         ('ReserchGate','https://www.researchgate.net/profile/Md-Rakibul-Hasan-13'),
#         ('Faculty Profile','https://www.bracu.ac.bd/about/people/md-rakibul-hasan'),
#         )

SOCIAL_WIDGET_NAME = ''

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

INDEX_SAVE_AS = 'blogs.html' # this is the index.html file inside the /theme/template folder

SLUGIFY_SOURCE = 'basename' # automatically, slug will be the filename

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False # will manually display categories using MENUITEMS
DISPLAY_PAGES_ON_MENU = False # will manually display pages using MENUITEMS

MENUITEMS = (
    ('home', '/'),
    ('about me', '/about_me'),
    ('publications', '/publications'),
    # ('teaching','/teaching'),
    ('activity', '/activity'),
    ('blogs','/blogs'),
    ('links','/links'),
    ('student corner', '/student_corner')
)

ARTICLE_PATHS = ['blogs']
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

# CSS_FILE='list.css'

# To compile faster: as suggested in https://github.com/getpelican/pelican/issues/2042#issuecomment-257620460
CONTENT_CACHING_LAYER = 'generator'
AUTHORS_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAGS_SAVE_AS = False