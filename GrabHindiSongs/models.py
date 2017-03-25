from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HindiSongArtist(models.Model):
	artist = models.TextField()
	artist_type = models.TextField(); 
	def __unicode__(self):
		return self.artist 

class HindiSongAlbum(models.Model):
	album = models.TextField()
	album_type = models.TextField();
	def __unicode__(self):
		return self.album 

class HindiSong(models.Model):
	song_name = models.TextField()
	song_url = models.TextField()
	album = models.ForeignKey(HindiSongAlbum,null=True)
	artist = models.ManyToManyField(HindiSongArtist)
	def __unicode__(self):
		return self.song_name
