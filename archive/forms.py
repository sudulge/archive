from django import forms
from archive.models import Movie, Book


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'content', 'thumbnail']
        labels = {
            'title': '제목',
            'content': '내용',
            'thumbnail': '대표이미지'
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'book_author', 'content', 'thumbnail']
        labels = {
            'title': '제목',
            'book_author': '지은이',
            'content': '내용',
            'thumbnail': '대표이미지'
        }