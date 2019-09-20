from django.shortcuts import render

def create_review(request):
    context  = {
        'title':'Create Review'
    }
    return render(request,'reviews/create-review.html', context)
