from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	datePublished = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Review(models.Model):
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

	def __str__(self):
		return self.content
