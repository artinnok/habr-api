from config.settings.base import *


DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': '',
        'PORT': '',
    }
}

ROOT_URLCONF = 'config.urls.production'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
