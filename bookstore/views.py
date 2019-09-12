from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Carlos',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 1, 2019'
    },
    
    {
        'author':'Jane',
        'title':'Blog Post 2',
        'content':'First post content',
        'date_posted':'August 2, 2019'
    }
]

# Create your views here.
def home(request):
    context  = {
        'posts':posts
    }
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html',{'title':'About'})