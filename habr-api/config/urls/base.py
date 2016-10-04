from django.conf.urls import url
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
]
