from django.conf.urls import url

from . import views

user_list = views.UserViewSet.as_view({
    'get': 'list',
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})

app_name = 'member'
urlpatterns = [
    url(r'^users/$',
        user_list,
        # views.UserList.as_view(),
        name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        user_detail,
        # views.UserDetail.as_view(),
        name='user_detail'),
]
