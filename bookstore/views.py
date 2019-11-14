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
