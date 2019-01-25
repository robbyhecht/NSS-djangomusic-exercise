from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Album, Song
from django.urls import reverse
from django.template import loader

def index(request):
  # return HttpResponse("Welcome to the music database.")
  print("REQUEST", request)
  artist_list = Artist.objects.order_by('name')
  context = {'artist_list': artist_list}
  return render(request, 'history/index.html', context)

def detail(request, artist_id):
  artist = get_object_or_404(Artist, pk=artist_id)

  # song_list = Song.objects.filter(artist_id = artist_id)
  context = {'artist': artist}
  return render(request, 'history/detail.html', context)

# ----

def newArtist(request):
  name = request.POST['artistName']
  q = Artist(name=name.title())
  q.save()
  return HttpResponseRedirect(reverse('history:index'))

def newSong(request, artist_id):
  artist = Artist.objects.get(id=artist_id)
  songInfo = request.POST['title']
  s = Song(title=title, album=3, artist=artist)
  s.save()
  return HttpResponseRedirect(reverse('history:detail', args=(artist.id,)))



# def addNewAlbum(request, artist_id):
#   artist = Artist.objects.get(id=artist_id)
#   # print(artist)
#   albumInfo = request.POST['title', 'release_year']
#   q = Album(album_name=title,release_year=release_year, artist=artist)
#   q.save()
#   return HttpResponseRedirect(reverse('history:artist_detail', args=(artist.id,)))
