from __future__ import absolute_import, unicode_literals
from celery import shared_task

import urllib2
import csv

from .celery import app

from bs4 import BeautifulSoup

from .models import HindiSong, HindiSongArtist, HindiSongAlbum

request_headers = {
"Host": "djraag.net",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en,en-US;q=0.8",
"Cookie": "__asc=d05a792d15a6cb153e1fc6c1aa0; __auc=d05a792d15a6cb153e1fc6c1aa0"
}

url_base  = "http://djraag.net"

url_base_hindi = "/latest-bollywood-movies-album-songs.html" 

@app.task
def fetch_page(page_no):
    page_url = "%s%s?page=%d"%(url_base,url_base_hindi,page_no)

    request = urllib2.Request(page_url)
    
    for header in request_headers:
        request.add_header(header, request_headers[header])
    
    web_page = urllib2.urlopen(request).read()
    soup = BeautifulSoup(web_page)

    all_albums =  soup.findAll("p", { "class" : "dj" })
    all_albums = all_albums[:25]
    
    for album in all_albums:
        album_url = album.a['href']
        
        print album.a.contents[0],
        
        new_album = HindiSongAlbum.objects.create(album=album.a.contents[0].strip())
        
        try :
            
            web_page  = urllib2.urlopen( url_base + album_url ).read()
            soup = BeautifulSoup(web_page)
            all_songs = soup.findAll("p", { "class" : "dj" })
            
            for song in all_songs[1:] :
                try :
                    song_url = song.a['href']
                    
                    web_page =  urllib2.urlopen(url_base + song_url).read()
                    soup = BeautifulSoup(web_page)
                    
                    all_songs = soup.findAll("p", { "class" : "dj" })
                    
                    artist = song.a.span.contents[0] if song.a.span is not None else song.span.contents[0] if song.span is not None else 'NA'  
                    new_artist = ''
                    try :
                        new_artist = HindiSongArtist.objects.get(artist=artist)
                    except : 
                        new_artist = HindiSongArtist.objects.create(artist=artist.strip())

                    new_song = ''
                    new_song  = HindiSong.objects.create(song_name=song.a.contents[0].strip(),song_url=all_songs[2].a['href'])
                    
                    new_song.album = new_album
                    new_song.artist.add(new_artist)
                    new_song.save()

                    print ".",

                except Exception as e:
                    print(str(e) )   
        except Exception as e:
            print 'completed of page :'            