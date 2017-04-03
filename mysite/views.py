from django.shortcuts import render
from GrabHindiSongs.models import HindiSongAlbum, HindiSong
from django.views.decorators.cache import cache_page

@cache_page(24 * 60 * 60 * 60)
def home_view(request):
   return render(request, 'index.html');

@cache_page(30 * 24 * 60 * 60 * 60)
def google_view(request):
	context = {}
	albums = HindiSongAlbum.objects.all()
	
	for album in albums:
		context[album] = HindiSong.objects.filter(album = album)



	return render(request,'index-google.html', {'context' : context })