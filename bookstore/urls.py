from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    path('books', views.books, name='bookstore-books'),
    path('Fantasy', views.Fantasy, name='Fantasy'),
    path('Horror', views.Horror, name='Horror'),
    path('Nonfiction', views.Nonfiction, name='Nonfiction'),
    path('Sciencefiction', views.Sciencefiction, name='Sciencefiction'),
    path('Thriller', views.Thriller, name='Thriller'),
    path('Satire', views.Satire, name='Satire'),
    path('Bestsellers', views.Bestsellers, name='Bestsellers'),
    path('authors/<id>', views.authors, name='authors'),
]
