from django.contrib import admin

# Register your models here.
from .models import HindiSong, HindiSongArtist, HindiSongAlbum

class HindiSongArtistAdmin(admin.ModelAdmin):
    pass

class HindiSongsAdmin(admin.ModelAdmin):
    pass

class HindiSongAlbumAdmin(admin.ModelAdmin):
    pass

admin.site.register(HindiSongArtist, HindiSongArtistAdmin)
admin.site.register(HindiSong, HindiSongsAdmin)
admin.site.register(HindiSongAlbum, HindiSongAlbumAdmin)