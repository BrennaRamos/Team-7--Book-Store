from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from reviews.views import reviews
from reviews.models import Review
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg

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

def Fantasy(request):
    book_list = Book.objects.all().filter(genre_id=1)
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
    return render(request,'bookstore/books-fantasy.html', {'books': books})

def Horror(request):
    book_list = Book.objects.all().filter(genre_id=3)
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
    return render(request,'bookstore/books-horror.html', {'books': books})

def Nonfiction(request):
    book_list = Book.objects.all().filter(genre_id=7)
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
    return render(request,'bookstore/books-nonfiction.html', {'books': books})

def Sciencefiction(request):
    book_list = Book.objects.all().filter(genre_id=2)
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
    return render(request,'bookstore/books-sciencefiction.html', {'books': books})

def Thriller(request):
    book_list = Book.objects.all().filter(genre_id=4)
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
    return render(request,'bookstore/books-thriller.html', {'books': books})


def Satire(request):
    book_list = Book.objects.all().filter(genre_id=8)
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
    return render(request,'bookstore/books-satire.html', {'books': books})

def Bestsellers(request):
    book_list = Book.objects.all().filter(publisher_id=6)
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
    return render(request,'bookstore/books-bestsellers.html', {'books': books})


def booksabc(request):
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
    return render(request,'bookstore/booksabc.html', {'books': books})

def Fantasyabc(request):
    book_list = Book.objects.all().filter(genre_id=1)
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
    return render(request,'bookstore/books-fantasyabc.html', {'books': books})

def Horrorabc(request):
    book_list = Book.objects.all().filter(genre_id=3)
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
    return render(request,'bookstore/books-horrorabc.html', {'books': books})

def Nonfictionabc(request):
    book_list = Book.objects.all().filter(genre_id=7)
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
    return render(request,'bookstore/books-nonfictionabc.html', {'books': books})

def Sciencefictionabc(request):
    book_list = Book.objects.all().filter(genre_id=2)
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
    return render(request,'bookstore/books-sciencefictionabc.html', {'books': books})

def Thrillerabc(request):
    book_list = Book.objects.all().filter(genre_id=4)
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
    return render(request,'bookstore/books-thrillerabc.html', {'books': books})


def Satireabc(request):
    book_list = Book.objects.all().filter(genre_id=8)
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
    return render(request,'bookstore/books-satireabc.html', {'books': books})

def Bestsellersabc(request):
    book_list = Book.objects.all().filter(publisher_id=6)
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
    return render(request,'bookstore/books-bestsellersabc.html', {'books': books})



def authors(request, id):
    author = get_object_or_404(Author, id=id)
    book_list = Book.objects.all().filter(author=author.id)
    # reviews = Review.objects.filter(author=id).order_by('-num_likes')
    # average_rating = reviews.aggregate(average=Avg('rating'))
    context = {
        'author': author,
        'books': book_list,
        #'averageRating': average_rating,
    }
    return render(request, 'bookstore/authors.html', context)

# Placeholder Views
#def book(request):
    #return render(request,'book_detail.html',{'title':'Book Details'})
#def author(request):
    #return render(request,'author_detail.html',{'title':'Author Details'})
#def wishlist(request):
    #return render(request,'wishlist_detail.html',{'title':'Wishlist Details'})
#def user(request):
    #return render(request,'user_detail.html',{'title':'User Details'})
