from django.db import models
from django.contrib.auth.models import User
from bookstore.models import Book

class Review(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	

	def __str__(self):
		return '{}-{}'.format(self.book.title, str(self.author.username))