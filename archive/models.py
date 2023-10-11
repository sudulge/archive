from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='archive/movie', null=True, blank=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='archive/book', null=True, blank=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title