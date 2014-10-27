"""
Django Local settings for letts_me project.

"""

from .development import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TheKnightsThatSayNi'

#ALLOWED_HOSTS = []

# Database
# Override with database engine
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# rename this file as local.py
