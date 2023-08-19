from .base import *
import os

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
PRODUCTION = os.environ.get('PRODUCTION')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles/' 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/', 'staticroot/')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/' 'media')



 
