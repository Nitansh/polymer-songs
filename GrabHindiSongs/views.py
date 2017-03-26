import json

from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core import serializers
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

from .models import HindiSongAlbum, HindiSongArtist, HindiSong


my_duplicate = {}

# Create your views here.
def album_view(request, page_no, query):
	page_no = int(page_no);
	if not query :
		all_albums = HindiSongAlbum.objects.all()[::-1][ (page_no - 1) * 4 :  page_no * 4 ]
	else :
		all_albums = HindiSongAlbum.objects.filter(Q(album__icontains=query))[ (page_no - 1) * 4 :  page_no * 4 ]

	posts_serialized = serializers.serialize('json', all_albums)
	return JsonResponse( json.loads(posts_serialized) , safe=False )

def artist_view(request, page_no, query):
	page_no = int(page_no);
	if not query :
		all_albums = HindiSongArtist.objects.all()[ (page_no - 1) * 4 :  page_no * 4 ]
	else :
		all_albums = HindiSongArtist.objects.filter(Q(artist__icontains=query))[ (page_no - 1) * 4 :  page_no * 4 ]

	posts_serialized = serializers.serialize('json', all_albums)
	return JsonResponse( json.loads(posts_serialized) , safe=False )


def song_view(request, album_name):
	fetched_album = ''
	try :
		fetched_album = HindiSongAlbum.objects.get(album=str(album_name))
	except MultipleObjectsReturned:
		fetched_result = HindiSongAlbum.objects.filter(album=str(album_name))
		if my_duplicate.get(album_name) :
			my_duplicate[album_name]['ctr'] = my_duplicate[album_name]['ctr'] + 1; 
			if my_duplicate[album_name]['ctr'] == my_duplicate[album_name]['max']:
				my_duplicate[album_name]['ctr'] = 0 
		else : 
			my_duplicate[album_name] = {}
			my_duplicate[album_name]['max'] = len(fetched_result)
			my_duplicate[album_name]['ctr'] = 0
		 
		fetched_album = HindiSongAlbum.objects.filter(album=str(album_name))[my_duplicate[album_name]['ctr']]

	all_songs = HindiSong.objects.filter(album=fetched_album.id)
	posts_serialized = serializers.serialize('json', all_songs)
	return JsonResponse( json.loads(posts_serialized) , safe=False )


def song_artist_view(request, album_name):
	fetched_album = ''
	try : 
		fetched_album = HindiSongArtist.objects.get(artist=str(album_name))
	except MultipleObjectsReturned:
		fetched_album = HindiSongArtist.objects.filter(artist=str(album_name)).order_by('-id').first()

	all_songs = HindiSong.objects.filter(artist=fetched_album.id)
	posts_serialized = serializers.serialize('json', all_songs)
	return JsonResponse( json.loads(posts_serialized) , safe=False )
