from django.contrib import admin

# Register your models here.
from .models import PanjabiSong, PanjabiSongArtist, PanjabiSongAlbum

class PanjabiSongArtistAdmin(admin.ModelAdmin):
    pass

class PanjabiSongsAdmin(admin.ModelAdmin):
    pass

class PanjabiSongAlbumAdmin(admin.ModelAdmin):
    pass

admin.site.register(PanjabiSongArtist, PanjabiSongArtistAdmin)
admin.site.register(PanjabiSong, PanjabiSongsAdmin)
admin.site.register(PanjabiSongAlbum, PanjabiSongAlbumAdmin)