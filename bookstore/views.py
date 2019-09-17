from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title':'Book 1',
        'author':'James Doe',
        'datePublished':'August 1, 2019'
    },
    
    {
        'title':'Book 2',
        'author':'Jane Doe',
        'datePublished':'August 2, 2019'
    }
]

# Create your views here.
def home(request):
    return render(request,'home.html')
def books(request):
    context  = {
        'posts':posts,
        'title':'Books'
    }
    return render(request,'books.html',context)
# Placeholder Views
#def book(request):
    #return render(request,'book_detail.html',{'title':'Book Details'})
#def author(request):
    #return render(request,'author_detail.html',{'title':'Author Details'})
#def wishlist(request):
    #return render(request,'wishlist_detail.html',{'title':'Wishlist Details'})
#def user(request):
    #return render(request,'user_detail.html',{'title':'User Details'})
