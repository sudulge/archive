from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from ..models import Movie
from ..forms import MovieForm


def movie_index(request):
    page = request.GET.get('page', '1')
    query = request.GET.get('query', '')
    movie_list = Movie.objects.order_by('create_date')
    if query:
        movie_list = movie_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()
    paginator = Paginator(movie_list, 10)
    page_obj = paginator.get_page(page)
    context = {'movie_list': page_obj, 'page': page, 'query': query}
    return render(request, 'archive/movie_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'archive/movie_detail.html', context)


@login_required(login_url='common:login')
def movie_create(request):
    if request.method == 'POST': # POST 요청 question_form.html 에서 저장하기 버튼을 클릭 했을 때
        form = MovieForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.create_date = timezone.now()
            movie.save()
            return redirect('archive:movie_index')
    else: # GET 요청 question_list.html 에서 질문 등록하기 버튼을 클릭 했을 때.
        form = MovieForm()
    context = {'form': form}
    return render(request, 'archive/movie_form.html', context)


@login_required(login_url='common:login')
def movie_modify(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user != movie.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('archive:movie_detail', movie_id=movie.id)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.modify_date = timezone.now()
            movie.save()
            return redirect('archive:movie_detail', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)
    context = {'form': form}
    return render(request, 'archive/movie_form.html', context)


@login_required(login_url='common:login')
def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user != movie.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('archive:movie_detail', movie_id=movie.id)
    movie.delete()
    return redirect('archive:movie_index')