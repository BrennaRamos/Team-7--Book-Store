from django.db import models

# Create your models here.
from bookstore.models import Book

class Cart(models.Model):
    items = models.ManyToManyField(Book, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "%s" %(self.id)