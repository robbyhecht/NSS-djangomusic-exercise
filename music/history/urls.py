from django.urls import path 
from . import views
from django.contrib import admin



app_name = 'history'
urlpatterns = [
    # ex: /artists/
    path('', views.index, name='index'),
    # ex: /artists/5/
    path('<int:artist_id>/', views.detail, name='detail'),
    # adds a new artist via form 
    path('addNewArtist/', views.newArtist, name='addArtist'),

    path('addNewSong/', views.newSong, name='addSong'),



]


