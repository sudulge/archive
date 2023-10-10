from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .models import Movie, Book
from .forms import MovieForm, BookForm
from django.core.paginator import Paginator

# Create your views here.

def movie_index(request):
    page = request.GET.get('page', '1')
    movie_list = Movie.objects.order_by('create_date')
    paginator = Paginator(movie_list, 10)
    page_obj = paginator.get_page(page)
    context = {'movie_list': page_obj}
    return render(request, 'archive/movie_list.html', context)

def book_index(request):
    page = request.GET.get('page', '1')
    book_list = Book.objects.order_by('create_date')
    paginator = Paginator(book_list, 10)
    page_obj = paginator.get_page(page)
    context = {'book_list': page_obj}
    return render(request, 'archive/book_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'archive/movie_detail.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'archive/book_detail.html', context)

def movie_create(request):
    if request.method == 'POST': # POST 요청 question_form.html 에서 저장하기 버튼을 클릭 했을 때
        form = MovieForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.create_date = timezone.now()
            movie.save()
            return redirect('archive:movie_index')
    else: # GET 요청 question_list.html 에서 질문 등록하기 버튼을 클릭 했을 때.
        form = MovieForm()
    context = {'form': form}
    return render(request, 'archive/movie_form.html', context)

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.create_date = timezone.now()
            book.save()
            return redirect('archive:book_index')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'archive/book_form.html', context)