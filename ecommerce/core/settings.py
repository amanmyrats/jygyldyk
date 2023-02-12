"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os 
import environ

from pathlib import Path

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR /  '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ because of casting above
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'rosetta',

    'django.forms',

    'webapps',
    'webapps.offer',
    'webapps.search',
    'webapps.customer',
    'webapps.address',
    'webapps.partner',
    'webapps.communication',
    'webapps.catalogue',
    'webapps.catalogue.reviews',
    'webapps.wishlists',
    'webapps.voucher',
    'webapps.basket',
    'webapps.checkout',
    'webapps.payment',
    'webapps.order',
    'webapps.shipping',
    'webapps.analytics',

    'webapps.dashboard',
    'webapps.dashboard.catalogue',
    'webapps.dashboard.communications',
    'webapps.dashboard.offers',
    'webapps.dashboard.orders',
    'webapps.dashboard.pages',
    'webapps.dashboard.partners',
    'webapps.dashboard.ranges',
    'webapps.dashboard.reports',
    'webapps.dashboard.reviews',
    'webapps.dashboard.shipping',
    'webapps.dashboard.users',
    'webapps.dashboard.vouchers',
    
    'utils',

    # # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'django_tables2',

    'sorl.thumbnail',

]

SITE_ID=1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'webapps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'webapps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'core.urls'

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")  # ROOT dir for templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            # os.path.join(BASE_DIR,django.__path__[0],'/forms/templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',

                'webapps.search.context_processors.search_form',
                'webapps.checkout.context_processors.checkout',
                'webapps.communication.notifications.context_processors.notifications',
                'core.context_processors.metadata',
            ],
            'libraries': {
                'basket_tags':'templatetags.basket_tags',
                'category_tags':'templatetags.category_tags',
                'currency_filters':'templatetags.currency_filters',
                'dashboard_tags':'templatetags.dashboard_tags',
                'datetime_filters':'templatetags.datetime_filters',
                'display_tags':'templatetags.display_tags',
                'form_tags':'templatetags.form_tags',
                'history_tags':'templatetags.history_tags',
                'image_tags':'templatetags.image_tags',
                'product_tags':'templatetags.product_tags',
                'purchase_info_tags':'templatetags.purchase_info_tags',
                'reviews_tags':'templatetags.reviews_tags',
                'shipping_tags':'templatetags.shipping_tags',
                'sorting_tags':'templatetags.sorting_tags',
                'string_filters':'templatetags.string_filters',
                'url_tags':'templatetags.url_tags',
                'wishlist_tags':'templatetags.wishlist_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DB", str(BASE_DIR / "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "aman"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "aman"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'tk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('tk', _('Turkmen')),
    ('en-us', _('English')),
    ('ru', _('Russian')),
)

LOCALE_PATHS = [
    Path(BASE_DIR, 'locale'),
]

ROSETTA_EXCLUDE_PATHS = ['venv',]
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
BING_APP_ID = None

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    BASE_DIR / "static_files",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'



SHOP_NAME = 'Internet Söwda Nokady'
SHOP_TAGLINE = ''
HOMEPAGE = reverse_lazy('catalogue:index')

# Dynamic class loading
DYNAMIC_CLASS_LOADER = 'core.loading.default_class_loader'

# Basket settings
BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
BASKET_COOKIE_OPEN = 'oscar_open_basket'
BASKET_COOKIE_SECURE = False
MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Recently-viewed products
RECENTLY_VIEWED_COOKIE_LIFETIME = 7 * 24 * 60 * 60
RECENTLY_VIEWED_COOKIE_NAME = 'oscar_history'
RECENTLY_VIEWED_COOKIE_SECURE = False
RECENTLY_VIEWED_PRODUCTS = 20

# Currency
DEFAULT_CURRENCY = 'TMT'

# Paths
IMAGE_FOLDER = 'images/products/%Y/%m/'
DELETE_IMAGE_FILES = True

# Copy this image from oscar/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
MISSING_IMAGE_URL = 'image_not_found.jpg'

# Address settings
# REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
#                                  'line4', 'postcode', 'country')
REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4')
# Pagination settings

OFFERS_PER_PAGE = 20
PRODUCTS_PER_PAGE = 20
REVIEWS_PER_PAGE = 20
NOTIFICATIONS_PER_PAGE = 20
EMAILS_PER_PAGE = 20
ORDERS_PER_PAGE = 20
ADDRESSES_PER_PAGE = 20
STOCK_ALERTS_PER_PAGE = 20
DASHBOARD_ITEMS_PER_PAGE = 20

# Checkout
ALLOW_ANON_CHECKOUT = False

# Reviews
ALLOW_ANON_REVIEWS = True
MODERATE_REVIEWS = False

# Accounts
ACCOUNTS_REDIRECT_URL = 'customer:profile-view'

# This enables sending alert notifications/emails instantly when products get
# back in stock by listening to stock record update signals.
# This might impact performance for large numbers of stock record updates.
# Alternatively, the management command ``oscar_send_alerts`` can be used to
# run periodically, e.g. as a cron job. In this case eager alerts should be
# disabled.
EAGER_ALERTS = True

# Registration
SEND_REGISTRATION_EMAIL = True
FROM_EMAIL = 'oscar@example.com'

# Slug handling
SLUG_FUNCTION = 'core.utils.default_slugifier'
SLUG_MAP = {}
SLUG_BLACKLIST = []
SLUG_ALLOW_UNICODE = False

# Cookies
COOKIES_DELETE_ON_LOGOUT = ['oscar_recently_viewed_products', ]

# Offers
OFFERS_INCL_TAX = False
# Values (using the names of the model constants) from
# "offer.ConditionalOffer.TYPE_CHOICES"
OFFERS_IMPLEMENTED_TYPES = [
    'SITE',
    'VOUCHER',
]

# Hidden Oscar features, e.g. wishlists or reviews
HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'fas fa-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'fas fa-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
            {
                'label': _('Options'),
                'url_name': 'dashboard:catalogue-option-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'fas fa-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'fas fa-users',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'fas fa-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
            {
                'label': _('Voucher Sets'),
                'url_name': 'dashboard:voucher-set-list',
            },

        ],
    },
    {
        'label': _('Content'),
        'icon': 'fas fa-folder',
        'children': [
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'fas fa-chart-bar',
        'url_name': 'dashboard:reports-index',
    },
]
DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'webapps.dashboard.nav.default_access_fn'  # noqa

# Search facets
SEARCH_FACETS = {
    'fields': {
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        'product_class': {'name': _('Type'), 'field': 'product_class'},
        'rating': {'name': _('Rating'), 'field': 'rating'},
        # You can specify an 'options' element that will be passed to the
        # SearchQuerySet.facet() call.
        # For instance, with Elasticsearch backend, 'options': {'order': 'term'}
        # will sort items in a facet by title instead of number of items.
        # It's hard to get 'missing' to work
        # correctly though as of Solr's hilarious syntax for selecting
        # items without a specific facet:
        # http://wiki.apache.org/solr/SimpleFacetParameters#facet.method
        # 'options': {'missing': 'true'}
    },
    'queries': {
        'price_range': {
            'name': _('Price range'),
            'field': 'price',
            'queries': [
                # This is a list of (name, query) tuples where the name will
                # be displayed on the front-end.
                (_('0 to 20'), '[0 TO 20]'),
                (_('20 to 40'), '[20 TO 40]'),
                (_('40 to 60'), '[40 TO 60]'),
                (_('60+'), '[60 TO *]'),
            ]
        },
    },
}

PRODUCT_SEARCH_HANDLER = None

THUMBNAILER = 'core.thumbnails.SorlThumbnail'

URL_SCHEMA = 'http'

SAVE_SENT_EMAILS_TO_DB = True

# Solr 6.x
HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        # 'URL': 'http://127.0.0.1:8983/solr/sandbox',
        # 'ADMIN_URL': 'http://127.0.0.1:8983/solr/admin/cores',
        # 'INCLUDE_SPELLING': True,
    },
}