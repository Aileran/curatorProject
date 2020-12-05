from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    date = models.DateField()
    genre = models.CharField(max_length=60)
    #rating
    comment = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField()
    #rating
    comment = models.TextField()
    director = models.CharField(max_length=60)
    studio = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)


class Album(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField()
    #rating
    comment = models.TextField()
    artist = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    label = models.CharField(max_length=60)

