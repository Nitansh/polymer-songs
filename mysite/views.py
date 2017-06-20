from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.views.generic.list import ListView

from GrabHindiSongs.models import HindiSongAlbum, HindiSong


@cache_page(24 * 60 * 60 * 60)
def home_view(request):
   return render(request, 'index.html');

class SongsListView(ListView):
    model = HindiSongAlbum
    template_name = 'index-google.html' 
    context_object_name = 'albums'  
    paginate_by = 10
    queryset = HindiSongAlbum.objects.all()[::-1]  # Default: Model.objects.all() 