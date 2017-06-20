import json

from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

from .models import HindiSongAlbum, HindiSongArtist, HindiSong

# Create your views here.
def album_view(request, page_no, query):
	page_no = int(page_no);
	if not query :
		all_albums = HindiSongAlbum.objects.all()[::-1][ (page_no - 1) * 4 :  page_no * 4 ]
	else :
		all_albums = HindiSongAlbum.objects.filter(Q(album__icontains=query))[ (page_no - 1) * 4 :  page_no * 4 ]

	if len(all_albums) == 0 :
		posts_serialized = [ {"fields" : { "album" : "we find following songs for you :)"}}]
	else :
		posts_serialized = json.loads( serializers.serialize('json', all_albums) )
	return JsonResponse( posts_serialized , safe=False )


def artist_view(request, page_no, query):
	page_no = int(page_no);
	if not query :
		all_albums = HindiSongArtist.objects.all()[ (page_no - 1) * 4 :  page_no * 4 ]
	else :
		all_albums = HindiSongArtist.objects.filter(Q(artist__icontains=query))[ (page_no - 1) * 4 :  page_no * 4 ]

	posts_serialized = serializers.serialize('json', all_albums)
	return JsonResponse( json.loads(posts_serialized) , safe=False )


def song_view(request, album_name, query):
	if album_name == 'search': 
		all_songs = HindiSong.objects.filter(Q(song_name__icontains=query))
	else :
		all_songs = HindiSong.objects.filter(album=album_name)
		
	posts_serialized = serializers.serialize('json', all_songs)
	return JsonResponse( json.loads(posts_serialized) , safe=False )

def song_view_template(request, album_name):
	if album_name == 'search': 
		all_songs = HindiSong.objects.filter(Q(song_name__icontains=query))
	else :
		all_songs = HindiSong.objects.filter(album=album_name)

	album = HindiSongAlbum.objects.get(pk=album_name)

	return render(request, 'songs.html', context={ "songs" : all_songs, "album" : album})

def song_artist_view(request, album_name):	
	all_songs = HindiSong.objects.filter(artist=album_name)
	posts_serialized = serializers.serialize('json', all_songs)
	return JsonResponse( json.loads(posts_serialized) , safe=False )
