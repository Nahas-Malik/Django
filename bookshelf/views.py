# bookshelf/views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'bookshelf/book_list.html', context)
