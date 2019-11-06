from django.db import models
from django.contrib.auth.models import User
from bookstore.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

# Review holds the history of reviews written by users
class Review(models.Model):
	content = models.CharField(max_length=800)
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	RATING_CHOICES = zip(range(1,6), range(1,6))
	rating = models.IntegerField(choices=RATING_CHOICES, default=1)
	anonymous = models.BooleanField(default=False)
	num_likes = models.IntegerField(default=0)

	def __str__(self):
		return '{}-{}'.format(self.book.title, str(self.author.username))

# Review_Like holds the history of reviews liked by users
class Review_Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, on_delete=models.CASCADE)

	def __str__(self):
		return '{}-{}'.format(self.review.id, str(self.user.username))