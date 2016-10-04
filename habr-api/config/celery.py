from django.conf import settings
from celery import Celery

app = Celery('celery')

app.config_from_envvar('DJANGO_SETTINGS_MODULE')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
