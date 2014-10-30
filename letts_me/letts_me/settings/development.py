"""
Django Development settings for letts_me project.

"""

from .common import *

DEBUG = True

TEMPLATE_DEBUG = True

COMPRESS_ENABLED = False

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

