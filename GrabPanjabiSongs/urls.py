from django.conf.urls import url

from .views import album_view, song_view, artist_view,song_artist_view


urlpatterns = [
    url(r'^(?P<page_no>\d+)/(?P<query>.*)/$', album_view, name='panjabi_album_view'),
    url(r'^artist/(?P<page_no>\d+)/(?P<query>.*)/$', artist_view, name='panjabi_artist_view'),
    url(r'^get-songs/(?P<album_name>.*)/(?P<query>.*)/$', song_view, name='panjabi_song_view'),
    url(r'^artist/get-songs/(?P<album_name>.*)/$', song_artist_view, name='panjabi_song_artist_view')
]