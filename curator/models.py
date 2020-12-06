from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.CharField(max_length=4)
    date_added = models.DateField(auto_now_add=True)
    #rating
    comment = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    studio = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.CharField(max_length=4)
    date_added = models.DateField(auto_now_add=True)
    #rating
    comment = models.TextField()


class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    label = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.CharField(max_length=4)
    date_added = models.DateField(auto_now_add=True)
    #rating
    comment = models.TextField()


