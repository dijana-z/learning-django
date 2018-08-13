from . import views
from django.urls import re_path

# defines to which app are the following urls referring to
app_name = 'music'

# re_path contains the url pattern that is a regular expression given as the first argument,
# the view function for the pattern and the name of the url shortcut used in the template
# NOTE: url() function was used in the tutorial, but there was a change in the newer Django versions
urlpatterns = [
    # matching: ../music/
    re_path(r'^$', views.IndexView.as_view(), name='index'),

    # matching: /music/album_no/
    # NOTE: detail view expects primary key, that is why the regex group is named pk
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # matching: /music/album/add/
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # matching: /music/album/album_no/
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpadte.as_view(), name='album-update'),

    # matching: /music/album/album_no/delete/
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # matching: ../music/register/
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
]
