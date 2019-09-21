from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Review
from .models import Author
from .models import Genre
from .models import Publisher

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)