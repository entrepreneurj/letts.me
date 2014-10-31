"""
Django Development settings for letts_me project.

"""

from .common import *

DEBUG = True

TEMPLATE_DEBUG = True

COMPRESS_ENABLED = False

# Defailt settings for social media
# In production, any soc. med. settings not overridden will be hidden.
GITHUB_PROFILE = 'github'
INSTAGRAM_PROFILE = 'instagram'
TWITTER_PROFILE = 'twitter'
FACEBOOK_PROFILE = 'facebook'

# Application definition

#INSTALLED_APPS += ()

#MIDDLEWARE_CLASSES += ()

#TEMPLATE_CONTEXT_PROCESSORS + = ()

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

