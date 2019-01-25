from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
      return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def __str__(self):
      return self.title

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # album = models.CharField(max_length=100)
    title = models.CharField(max_length=100)