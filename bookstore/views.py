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
<<<<<<< Updated upstream
def home(request):
    return render(request,'home.html')
=======
>>>>>>> Stashed changes
def books(request):
    context  = {
        'posts':posts,
        'title':'Books'
    }
<<<<<<< Updated upstream
    return render(request,'books.html',context)
=======
    return render(request,'books/books.html',context)

def cart(request):
    return render(request,'cart.html',{'title':'Cart'})


>>>>>>> Stashed changes
# Placeholder Views
#def book(request):
    #return render(request,'book_detail.html',{'title':'Book Details'})
#def author(request):
    #return render(request,'author_detail.html',{'title':'Author Details'})
#def wishlist(request):
    #return render(request,'wishlist_detail.html',{'title':'Wishlist Details'})
#def user(request):
    #return render(request,'user_detail.html',{'title':'User Details'})
