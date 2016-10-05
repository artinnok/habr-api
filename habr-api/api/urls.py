from django.conf.urls import url

from api.views import AuthorList


urlpatterns = [
    url(
        regex='^authors/',
        view=AuthorList.as_view(),
        name='authors'
    )
]