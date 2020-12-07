from django.db import models

#each is a model of one type of media: book, movie, or album
class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.DateField()
    #date_added = models.DateField(auto_now_add=True)
    #rating = models.IntegerChoices
    #comment = models.TextField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    studio = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.DateField()
    #date_added = models.DateField(auto_now_add=True)
    #rating
    #comment = models.TextField()

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    label = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    year = models.DateField()
    #date_added = models.DateField(auto_now_add=True)
    #rating
    #comment = models.TextField()

    def __str__(self):
        return self.title
