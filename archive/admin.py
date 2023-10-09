from django.contrib import admin
from .models import Movie, Book

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author', 'content']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Book, BookAdmin)