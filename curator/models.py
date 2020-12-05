from django.db import models

# Create your models here.
#book entry for book form
class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    date = models.DateField()
    #rating
    comment = models.TextField()
