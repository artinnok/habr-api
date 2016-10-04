from django.conf import settings
from django.conf.urls.static import static

from config.urls.base import *
from core.views import error404


urlpatterns = urlpatterns + [
    url(
        regex=r'^error404/$',
        view=error404,
        name='error404'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
