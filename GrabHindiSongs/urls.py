from django.conf.urls import url

from .views import album_view, song_view


urlpatterns = [
    url(r'^(?P<page_no>\d+)/$', album_view, name='album_view'),
    url(r'^get-songs/(?P<album_name>.*)/$', song_view, name='song_view')
]