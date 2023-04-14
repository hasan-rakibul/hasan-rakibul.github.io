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

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('Google Scholar','https://scholar.google.com.au/citations?user=DuCQ8goAAAAJ&hl=en'),
        ('ReserchGate','https://www.researchgate.net/profile/Md-Rakibul-Hasan-10'),
        ('LinkedIn','https://www.linkedin.com/in/m-rakibul'),
        ('GitHub','https://github.com/hasan-rakibul'),
        ('ORCiD','https://orcid.org/0000-0003-2565-5321'),
        ('BRAC University','https://www.bracu.ac.bd/about/people/md-rakibul-hasan'),
        # ('Web of Science','https://www.webofscience.com/wos/author/rid/AFK-8839-2022'),
        ('e-mail','mailto:Rakibul.Hasan@curtin.edu.au'),
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
    ('blogs','/category/blogs.html'),
    ('student corner', '/student_corner')
)

ARTICLE_PATHS = ['blogs']
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

# CSS_FILE='list.css'