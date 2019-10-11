from django.shortcuts import render
from .models import Review
from bookstore.models import Book, Book_User
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Avg

def reviews(request, id, title):
	user = request.user
	book = get_object_or_404(Book, id=id, title=title)
	reviews = Review.objects.filter(book=book).order_by('-id')
	average_rating = reviews.aggregate(average=Avg('rating'))
	if user.is_authenticated:
		this_user_review = reviews.filter(author=user)
		reviews_minus_this_user = reviews.exclude(author=user)
		purchased = Book_User.objects.filter(book=book, user=user).exists()
		reviewed_already = Review.objects.filter(book=book, author=user).exists()
	else:
		this_user_review =  None
		reviews_minus_this_user = reviews
		review_form = ReviewForm(request.POST or None)
		purchased = None
		reviewed_already = None

	if request.method == 'POST':
		if Review.objects.filter(book=book, author=user).exists():
			messages.warning(request, "You can only review a book once.")
			review_form = ReviewForm(request.POST or None)
		else:
			review_form = ReviewForm(request.POST or None)
			if review_form.is_valid():
				content = request.POST.get('content')
				rating = request.POST.get('rating')
				review = Review.objects.create(book=book, author=user, content=content, rating=rating)
				review.save()
				messages.success(request, "You've successfully reviewed this book.")
				review_form= ReviewForm()
			else:
				review_form= ReviewForm()
	else:
		review_form= ReviewForm()

	context = {
    	'title': 'Reviews',
    	'reviews': reviews,
    	'this_user_review': this_user_review,
    	'reviews_minus_this_user': reviews_minus_this_user,
    	'review_form': review_form,
    	'book_title': book.title,
    	'average_rating': average_rating['average'],
    	'user': user,
    	'purchased': purchased,
    	'reviewed_already': reviewed_already,
    }
	return render(request, 'reviews/reviews.html', context)