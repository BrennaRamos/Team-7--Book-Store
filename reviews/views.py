from django.shortcuts import render
from .models import Review
from bookstore.models import Book, Book_User
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Avg

def reviews(request, id, title):
	book = get_object_or_404(Book, id=id, title=title)
	reviews = Review.objects.filter(book=book).order_by('-id')
	average_rating = reviews.aggregate(average=Avg('rating'))
	if request.method == 'POST':
		user = request.user
		if user.is_authenticated:
			review_form = ReviewForm(request.POST or None)
			if review_form.is_valid() and Book_User.objects.filter(book=book, user=user).exists():
				content = request.POST.get('content')
				rating = request.POST.get('rating')
				review = Review.objects.create(book=book, author=user, content=content, rating=rating)
				review.save()
				messages.success(request, "You've successfully reviewed this book.")
				return HttpResponseRedirect(request.path_info)
			else:
				messages.warning(request, "You must purchase this book in order to review it.")
				review_form= ReviewForm()
		else:
			messages.warning(request, "You must be logged in to write a review.")
			review_form= ReviewForm()
	else:
		review_form= ReviewForm()

	context = {
    	'title': 'Reviews',
    	'reviews': reviews,
    	'review_form': review_form,
    	'book_title': book.title,
    	'average_rating': average_rating['average']
    }
	return render(request, 'reviews/reviews.html', context)