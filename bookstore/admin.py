from django.contrib import admin

# Register your models here.
from .models import Book, Author, Genre, Publisher, Book_User

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book_User)