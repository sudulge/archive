from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from ..models import Book
from ..forms import BookForm


def book_index(request):
    page = request.GET.get('page', '1')
    query = request.GET.get('query', '')
    book_list = Book.objects.order_by('create_date')
    if query:
        book_list = book_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(book_author__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()
    paginator = Paginator(book_list, 10)
    page_obj = paginator.get_page(page)
    context = {'book_list': page_obj, 'page': page, 'query': query}
    return render(request, 'archive/book_list.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'archive/book_detail.html', context)


@login_required(login_url='common:login')
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.create_date = timezone.now()
            book.save()
            return redirect('archive:book_index')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'archive/book_form.html', context)


@login_required(login_url='common:login')
def book_modify(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user != book.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('archive:book_detail', book_id=book.id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.modify_date = timezone.now()
            book.save()
            return redirect('archive:book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'archive/book_form.html', context)


@login_required(login_url='common:login')
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user != book.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('archive:book_detail', book_id=book.id)
    book.delete()
    return redirect('archive:book_index')