from django import forms
from django.forms import ModelForm
from .models import PanjabiSongArtist, PanjabiSongAlbum, PanjabiSong

class PanjabiSongArtistForm(ModelForm):
    class Meta:
        model = PanjabiSongArtist

class PanjabiSongAlbumForm (ModelForm):
    class Meta:
        model = PanjabiSongAlbum

class PanjabiSongForm (ModelForm):
    class Meta:
        model = PanjabiSong