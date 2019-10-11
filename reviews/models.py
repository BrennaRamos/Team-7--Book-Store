from django.db import models
from django.contrib.auth.models import User
from bookstore.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	RATING_CHOICES = zip(range(1,6), range(1,6))
	rating = models.IntegerField(choices=RATING_CHOICES, default=1)
	ANONYMITY_CHOICES = [
	("Username", "Username"),
    ("Anonymous", "Anonymous"),
    ("Full Name", "Full Name"),
    ]
	anonymity = models.CharField(max_length=50, choices=ANONYMITY_CHOICES, default='Username')

	def __str__(self):
		return '{}-{}'.format(self.book.title, str(self.author.username))