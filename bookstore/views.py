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