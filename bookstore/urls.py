from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    path('about/', views.about, name='bookstore-about')
    # path('<int:book_id>/book', views.book_detail, name = 'book_detail')    -- these paths are placeholders as ideas
    # path('<int:author_id>/author', views.author_detail, name = 'author_detail')
    # path('<int:wishlist_id>/wishlist', views.wishlist_detail, name = 'wishlist_detail')
    # path('<int:user_id>/user', views.user_detail, name = 'user_detail')
]
