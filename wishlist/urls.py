from django.urls import path
from . import views
from wishlist.views import WishlistNameList

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/rename_wish', views.rename_wish, name = 'rename_wish'),
    path('wishlists/', WishlistNameList.as_view(), name= 'wishlists'),
]
