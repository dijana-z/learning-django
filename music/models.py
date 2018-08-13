from django.db import models
# NOTE: the next line in original tutorial was 'from django.core.urlresolvers import reverse'
#       but was changed because of the version difference
from django.urls import reverse


class Album(models.Model):
    """
    Album model that will be translated into album table in our database
    """
    # defining the variables (table columns)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse(viewname='music:detail', kwargs={'pk': self.id})

    def __str__(self):
        """
        :return: string representation of the album
        """
        return "Artist: " + self.artist + " , Title: " + self.album_title


class Song(models.Model):
    """
    Song model that will be translated into song table in our database
    """
    # defining the variables (table columns)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        """
        :return: string representation of the song
        """
        return "Title: " + self.song_title


