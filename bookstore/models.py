from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.


class Author(models.Model):
	name = models.CharField(max_length=50)
	biography = models.CharField(max_length=500)
	
	def __str__(self):
		return self.name

class Genre(models.Model):
	genre = models.CharField(max_length=50)

	def __str__(self):
		return self.genre

class Publisher(models.Model):
	publisher = models.CharField(max_length=50)
	pubLocation = models.CharField(max_length=50)

	def __str__(self):
		return self.publisher

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	datePublished = models.DateField()
	bookDescription = models.TextField(null=True)
	genre = models.ForeignKey(Genre, on_delete=models.SET('Default'))
	publisher = models.ForeignKey(Publisher, on_delete=models.SET('Default'))
	price = models.DecimalField(max_digits=5, decimal_places=2)
	photo = models.ImageField(upload_to="gallery")
	aveRating = models.DecimalField(max_digits=3, decimal_places=1, default=0)

	class Meta:
		ordering = ['price']

	def __str__(self):
		return self.title

# Book_User hold the history of books purchased by users.
class Book_User(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

	def __str__(self):
		return '{}-{}'.format(self.book.title, str(self.user.username))