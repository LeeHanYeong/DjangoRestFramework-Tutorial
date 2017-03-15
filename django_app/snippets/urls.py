from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import cbv
snippet_list = cbv.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = cbv.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
snippet_highlight = cbv.SnippetViewSet.as_view({
    'get': 'highlight',
})

app_name = 'snippets'
urlpatterns = [
    url(r'^snippets/$',
        # cbv.SnippetList.as_view(),
        snippet_list,
        name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        # cbv.SnippetDetail.as_view(),
        snippet_detail,
        name='snippet_detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        # cbv.SnippetHighlight.as_view(),
        snippet_highlight,
        name='snippet_highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
