from config.settings.base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}

ROOT_URLCONF = 'config.urls.local'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
