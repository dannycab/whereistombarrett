SITENAME = "whereistombarrett"
SITEURL = ""
PATH = "content"
THEME = "themes/punk"
TIMEZONE = "America/Detroit"
DEFAULT_LANG = "en"

# Single page site — no articles, no feeds
ARTICLE_PATHS = []
PAGE_PATHS = ["pages"]
DIRECT_TEMPLATES = []
PAGINATED_TEMPLATES = {}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
RELATIVE_URLS = True

# Copy CNAME into output for GitHub Pages custom domain
STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}

OUTPUT_PATH = "docs"
