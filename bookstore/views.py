from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    context  = {
        'books': Book.objects.all(),
        'title':'Home'
    }
    return render(request,'bookstore/home.html', context)

def books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    #context  = {
    #    'books': Book.objects.all(),
    #    'title':'Books'
    #}
    return render(request,'bookstore/books.html', {'books': books})

# Placeholder Views
#def book(request):
    #return render(request,'book_detail.html',{'title':'Book Details'})
#def author(request):
    #return render(request,'author_detail.html',{'title':'Author Details'})
#def wishlist(request):
    #return render(request,'wishlist_detail.html',{'title':'Wishlist Details'})
#def user(request):
    #return render(request,'user_detail.html',{'title':'User Details'})
