from django.urls import path
from . import views

urlpatterns = [
    path(r'reviews/<id>/<title>', views.reviews, name='reviews'),
    path(r'review/update/<id>', views.updateReview, name='updateReview'),
    path(r'review/delete/<id>', views.deleteReview, name='deleteReview'),
]