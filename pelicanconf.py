AUTHOR = 'M Rakibul Hasan (Rakib)'
SITENAME = 'M Rakibul Hasan (Rakib)'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images','extras','pdfs']
EXTRA_PATH_METADATA = {
        'extras/favicon.ico': {'path': 'favicon.ico'},
}

# specify the custom theme directory
THEME = 'theme'

TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('Google Scholar','https://scholar.google.com/citations?user=DuCQ8goAAAAJ&hl=en'),
        ('ReserchGate','https://www.researchgate.net/profile/M-Rakibul-Hasan'),
        ('LinkedIn','https://www.linkedin.com/in/m-rakibul'),
        ('GitHub','https://github.com/mrh-rakib'),
        ('ORCiD','https://orcid.org/0000-0003-2565-5321'),
        ('Faculty Profile','https://www.bracu.ac.bd/about/people/md-rakibul-hasan'),
        ('publons','https://publons.com/researcher/5018248/md-rakibul-hasan/'),
        ('e-mail','mailto:rakibul.hasan@bracu.ac.bd'),
        )

LINKS_WIDGET_NAME = 'find me on'

# Social widget
# SOCIAL = (
#         ('e-mail','mailto:rakibul.hasan@bracu.ac.bd'),
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

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False # will manually display categories using MENUITEMS
DISPLAY_PAGES_ON_MENU = False # will manually display pages using MENUITEMS

MENUITEMS = (
#     ('home', '/'),
    ('about me', '/me'),
    ('r&d', '/rnd'),
    ('student projects', '/student_projects'),
    ('teaching','/teaching'),
    ('activity', '/activity'),
)
