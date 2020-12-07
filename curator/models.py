from django.db import models
from django.contrib.auth.models import User

#each is a model of one type of media: book, movie, or album
class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60, blank=True)
    publisher = models.CharField(max_length=60, blank=True)
    genre = models.CharField(max_length=60, blank=True)
    year = models.DateField(blank=True)
    #date_added = models.DateField(auto_now_add=True)
    #rating = models.IntegerField(blank=True, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=60)
    director = models.CharField(max_length=60, blank=True)
    studio = models.CharField(max_length=60, blank=True)
    genre = models.CharField(max_length=60, blank=True)
    year = models.DateField(blank=True)
    #date_added = models.DateField(auto_now_add=True)
    #rating = models.IntegerField(blank=True, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60, blank=True)
    label = models.CharField(max_length=60, blank=True)
    genre = models.CharField(max_length=60, blank=True)
    year = models.DateField(blank=True)
    #date_added = models.DateField(auto_now_add=True)
    #rating = models.IntegerField(blank=True, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
