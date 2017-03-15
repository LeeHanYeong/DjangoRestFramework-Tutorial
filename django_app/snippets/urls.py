from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import cbv

app_name = 'snippets'
urlpatterns = [
    url(r'^snippets/$',
        cbv.SnippetList.as_view(),
        name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        cbv.SnippetDetail.as_view(),
        name='snippet_detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        cbv.SnippetHighlight.as_view(),
        name='snippet_highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
