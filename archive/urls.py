from django.urls import path

from .views import base_views, movie_views, book_views

app_name = 'archive'


urlpatterns = [
    # base_views.py

    # movie_views.py
    path('', movie_views.movie_index, name='movie_index'),
    path('movie/', movie_views.movie_index, name='movie_index'),
    path('movie/<int:movie_id>/', movie_views.movie_detail, name='movie_detail'),
    path('movie/create', movie_views.movie_create, name='movie_create'),
    path('movie/modify/<int:movie_id>', movie_views.movie_modify, name='movie_modify'),
    path('movie/delete/<int:movie_id>', movie_views.movie_delete, name='movie_delete'),

    # book_views.py
    path('book/', book_views.book_index, name='book_index'),
    path('book/<int:book_id>/', book_views.book_detail, name='book_detail'),
    path('book/create', book_views.book_create, name='book_create'),
    path('book/modify/<int:book_id>', book_views.book_modify, name='book_modify'),
    path('book/delete/<int:book_id>', book_views.book_delete, name='book_delete'),
]