import json

from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core import serializers

from .models import HindiSongAlbum, HindiSongArtist, HindiSong

# Create your views here.
def album_view(request, page_no):
	all_albums = HindiSongAlbum.objects.all()[ (page_no - 1) * 4 :  page_no * 4 ]
	posts_serialized = serializers.serialize('json', all_albums)
	return JsonResponse( json.loads(posts_serialized) , safe=False )

def song_view(request, album_name):
	fetched_album = HindiSongAlbum.objects.get(album=str(album_name))
	all_songs = HindiSong.objects.filter(album=fetched_album.id)
	posts_serialized = serializers.serialize('json', all_songs)
	return JsonResponse( json.loads(posts_serialized) , safe=False )
