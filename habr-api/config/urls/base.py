from django.conf.urls import url, include
from django.contrib import admin

from core.views import IndexView

urlpatterns = [
    url(
        regex=r'^$',
        view=IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^admin/',
        view=admin.site.urls
    ),
    url(
        regex=r'^api/',
        view=include('api.urls', namespace='api')
    )
]
