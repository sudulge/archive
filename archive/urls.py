from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'archive'


urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('movie/', views.movie_index, name='movie_index'),
    path('book/', views.book_index, name='book_index'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('movie/create', views.movie_create, name='movie_create'),
    path('book/create', views.book_create, name='book_create'),
]