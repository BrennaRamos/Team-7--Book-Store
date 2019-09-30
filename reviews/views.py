from django.shortcuts import render
from .models import Review
from bookstore.models import Book
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def reviews(request, id, title):
	book = get_object_or_404(Book, id=id, title=title)
	reviews = Review.objects.filter(book=book).order_by('-id')
	if request.method == 'POST':
		review_form = ReviewForm(request.POST or None)
		if review_form.is_valid():
			content = request.POST.get('content')
			review = Review.objects.create(book=book, author=request.user, content=content)
			review.save()
			return HttpResponseRedirect(request.path_info)
	else:
			review_form= ReviewForm()

	context = {
    	'title': 'Reviews',
    	'reviews': reviews,
    	'review_form': review_form,
    	'book_title': book.title
    }
	return render(request, 'reviews/reviews.html', context)