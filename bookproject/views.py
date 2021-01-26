from django.shortcuts import render, HttpResponse,redirect
from .models import Book

def test(request):
    book_list = Book.objects.all()
    return render(request, "book.html", {"book_list": book_list})


def add_book(request):
    form = request.POST
    text = form["book_text"]
    book = Book(text=text)
    book.save()
    return redirect(test)





    
