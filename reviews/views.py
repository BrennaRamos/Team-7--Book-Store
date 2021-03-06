from django.shortcuts import render
from .models import Review, Review_Like
from bookstore.models import Book, Book_User, Author, Genre, Publisher
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Avg
import datetime


def reviews(request, id, title):
    user = request.user
    book = get_object_or_404(Book, id=id, title=title)
    reviews = Review.objects.filter(book=book).order_by('-num_likes')

    if user.is_authenticated:
        this_user_review = reviews.filter(author=user)
        reviews_minus_this_user = reviews.exclude(author=user)
        purchased = Book_User.objects.filter(book=book, user=user).exists()
        reviewed_already = Review.objects.filter(book=book, author=user).exists()
    else:
        this_user_review = None
        reviews_minus_this_user = reviews
        review_form = ReviewForm(request.POST or None)
        purchased = None
        reviewed_already = None

    if request.method == 'POST':
        review_form = ReviewForm(request.POST or None)
        if review_form.is_valid():
            content = request.POST.get('content')
            rating = request.POST.get('rating')
            if request.POST.get('anonymous'):
                anonymous = True
            else:
                anonymous = False
            review = Review.objects.create(book=book, author=user, content=content, rating=rating, anonymous=anonymous)
            review.save()
            average_rating = reviews.aggregate(average=Avg('rating'))
            book.aveRating = average_rating['average']
            book.save()
            messages.success(request, "You've successfully reviewed this book.")
            return HttpResponseRedirect('/reviews/%s/%s' % (book.id, book.title))
        else:
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    context = {
        'title': 'Reviews',
        'reviews': reviews,
        'this_user_review': this_user_review,
        'reviews_minus_this_user': reviews_minus_this_user,
        'review_form': review_form,
        'book_title': book.title,
        'book_id': book.id,
        'average_rating': book.aveRating,
        'user': user,
        'purchased': purchased,
        'reviewed_already': reviewed_already,
        'book_author': book.author,
        'book_authordesc': book.author.biography,
        'book_desc': book.bookDescription,
        'book_genre': book.genre,
        'book_publisher': book.publisher,
        'book_pubdate': book.datePublished,
        'book_photo': book.photo,
        'book_price': book.price,
    }
    return render(request, 'reviews/reviews.html', context)
    
def updateReview(request, id):
    review = get_object_or_404(Review, id=id)
    if review:
        update_review_form = UpdateReviewForm(request.POST or None, initial={'content': review.content, 'rating': review.rating, 'anonymous': review.anonymous})

    if update_review_form.is_valid():
        review.content = request.POST.get('content')
        review.rating = request.POST.get('rating')
        review.date_posted = datetime.datetime.now()
        if request.POST.get('anonymous'):
            review.anonymous = True 
        else:
            review.anonymous = False 
        review.save()
        book = get_object_or_404(Book, id=review.book.id)
        reviews = Review.objects.filter(book=book).order_by('-num_likes')
        average_rating = reviews.aggregate(average=Avg('rating'))
        book.aveRating = average_rating['average']
        book.save()
        return HttpResponseRedirect('/reviews/%s/%s' % (review.book.id, review.book.title))
                
    context = {
        'title': 'Update Review',
        'update_review_form': update_review_form,
        'book_title': review.book.title,
    }
    return render(request, 'reviews/update-review.html', context)


def deleteReview(request, id):
    review = get_object_or_404(Review, id=id)
    if request.GET.get('Delete') == 'Delete':
        review.delete()
        book = get_object_or_404(Book, id=review.book.id)
        reviews = Review.objects.filter(book=book).order_by('-num_likes')
        average_rating = reviews.aggregate(average=Avg('rating'))
        if average_rating['average']:
            book.aveRating = average_rating['average']
        else:
            book.aveRating = 0;
        book.save()
        return HttpResponseRedirect('/reviews/%s/%s' % (review.book.id, review.book.title))
    elif request.GET.get('Cancel') == 'Cancel':
        return HttpResponseRedirect('/reviews/%s/%s' % (review.book.id, review.book.title))

    context = {
        'title': 'Delete Review',
        'book_title': review.book.title,
    }
    return render(request, 'reviews/delete-review.html', context)

def likeReview(request, id):
    user = request.user
    review = get_object_or_404(Review, id=id)
    liked_already = Review_Like.objects.filter(user=user, review=review).exists()

    if request.GET.get('Like') == 'Like':
        like = Review_Like.objects.create(user=user, review=review)
        like.save()
        review.num_likes = Review_Like.objects.filter(review=review).count()
        review.save()
        return HttpResponseRedirect('/review/more/%s' % review.id)

    elif request.GET.get('Dislike') == 'Dislike':
        like = get_object_or_404(Review_Like, review=review)
        like.delete()
        review.num_likes = Review_Like.objects.filter(review=review).count()
        review.save()
        return HttpResponseRedirect('/review/more/%s' % review.id)
    elif request.GET.get('Back') == 'Back':
        return HttpResponseRedirect('/reviews/%s/%s' % (review.book.id, review.book.title))

    context = {
        'title': 'Like Review',
        'liked_already': liked_already,
        'review': review,
    }

    return render(request, 'reviews/like-review.html', context)

