"""
Django Local settings for letts_me project.

"""

from .production import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f9-ecmr04m5094u5,3p0]ri]cfasfjdpf,'

ALLOWED_HOSTS = ['your-domain-here.tld']

# Database
# Override database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = '/full/path/to/static_root'
MEDIA_ROOT = '/full/path/to/media_root'
# rename this file as local.py
