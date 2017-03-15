from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import cbv

app_name = 'snippet'
urlpatterns = [
    url(r'^snippets/$',
        cbv.SnippetList.as_view(),
        name='list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        cbv.SnippetDetail.as_view(),
        name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
