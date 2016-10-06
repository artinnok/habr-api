from django.conf.urls import url

from api.views import AuthorList, AuthorDetail, idf


urlpatterns = [
    url(
        regex=r'^authors/$',
        view=AuthorList.as_view(),
        name='author_list'
    ),
    url(
        regex=r'^authors/(?P<pk>[0-9]+)/$',
        view=AuthorDetail.as_view(),
        name='author_detail'
    ),
    url(
        regex=r'^posts/(?P<pk>[0-9]+)/$',
        view=idf,
        name='idf'
    )
]