from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    path('books/', views.books, name='bookstore-books'),
    path('create-review/', views.createReview, name='bookstore-create-review')
]

 # These paths are placeholders as ideas

#app_name = 'book'
#urlpatterns = [
    #path('<int:book_id>/book/', views.book_detail, name = 'book_detail')
#]

#app_name = 'author'
#urlpatterns = [
    #path('<int:author_id>/author/', views.author_detail, name = 'author_detail')
#]

#app_name = 'wishlist'
#urlpatterns = [
    # path('<int:wishlist_id>/wishlist/', views.wishlist_detail, name = 'wishlist_detail')
#]

#app_name = 'user'
#urlpatterns = [
    # path('<int:user_id>/user/', views.user_detail, name = 'user_detail')
#]
