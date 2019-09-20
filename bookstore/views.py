from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Review
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request,'home.html')

def books(request):
    context  = {
        'posts': Book.objects.all(),
        'title':'Books'
    }
    return render(request,'books.html', context)

# Placeholder Views
#def book(request):
    #return render(request,'book_detail.html',{'title':'Book Details'})
#def author(request):
    #return render(request,'author_detail.html',{'title':'Author Details'})
#def wishlist(request):
    #return render(request,'wishlist_detail.html',{'title':'Wishlist Details'})
#def user(request):
    #return render(request,'user_detail.html',{'title':'User Details'})
