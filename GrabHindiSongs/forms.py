from django import forms
from django.forms import ModelForm
from .models import HindiSongArtist, HindiSongAlbum, HindiSong

class HindiSongArtistForm(ModelForm):
    class Meta:
        model = HindiSongArtist

class HindiSongAlbumForm (ModelForm):
    class Meta:
        model = HindiSongAlbum

class HindiSongForm (ModelForm):
    class Meta:
        model = HindiSong