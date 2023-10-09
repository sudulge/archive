from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='archive/movie', null=True, blank=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='archive/book', null=True, blank=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title