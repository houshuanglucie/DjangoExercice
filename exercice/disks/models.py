from django.db import models


class Artist(models.Model):
    Name = models.CharField(max_length=120, verbose_name="nom de l'artiste")

    class Meta:
        verbose_name = "artiste"

    def __str__(self):
        return self.Name


class Album(models.Model):
    Title = models.CharField(max_length=200, verbose_name="titre de l'album")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, verbose_name="artiste")

    def __str__(self):
        return self.Title


class Track(models.Model):
    Name = models.CharField(max_length=200, verbose_name="nom")
    Album = models.ForeignKey('Album', on_delete=models.CASCADE)
    Composer = models.CharField(max_length=220, verbose_name="compositeur")
    Milliseconds = models.TextField(verbose_name="duree")
    Bytes = models.IntegerField()
    UnitPrice = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="prix unitaire")

    def __str__(self):
        return self.Name
