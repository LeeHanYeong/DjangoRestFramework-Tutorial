from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^users/$',
        views.UserList.as_view(),
        name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user_detail'),
]
