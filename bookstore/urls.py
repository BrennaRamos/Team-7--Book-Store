from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    path('books/', views.books, name='bookstore-books'),
    path('authors/<id>', views.authors, name='authors'),
]
