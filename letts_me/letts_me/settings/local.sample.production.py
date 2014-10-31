"""
Django Local settings for letts_me project.

"""

from .production import *

# Site title used in templates
SITE_TITLE = "your-site-title-here"

# In production, any soc. med. settings not overridden will be hidden.
#GITHUB_PROFILE = 'your-username-here' 
#INSTAGRAM_PROFILE = 'your-user-name-here'
#TWITTER_PROFILE = 'your-handle-here'
#FACEBOOK_PROFILE = 'your-facebook-id-here'

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
