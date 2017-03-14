from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import fbv, cbv

urlpatterns = [
    url(r'^snippets/$', cbv.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', cbv.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
