"""
Django Development settings for letts_me project.

"""

from .common import *

DEBUG = TEMPLATE_DEBUG = False

COMPRESS_ENABLED = True

# Application definition

INSTALLED_APPS += (
    # For reporting errors to Sentry (getsentry.com)
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
        'dsn': 'OVERRIDE_IN_LOCAL_PY',
}

#MIDDLEWARE_CLASSES += ()


# SITE_TEMPLATE_CONSTANTS
SITE_TITLE = 'Letts.me'
GITHUB_PROFILE = 'entrepreneurj'
INSTAGRAM_PROFILE = 'blogginglife'
TWITTER_PROFILE = 'jal08'
FACEBOOK_PROFILE = None


#TEMPLATE_CONTEXT_PROCESSORS + = ()

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

