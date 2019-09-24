from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='bookstore-home'),
    path('cart', views.cart_home, name='cart'),
    path('addtocart/<int:book_id>',views.add_to_cart, name='addtocart'),
    path('removefromcart/<int:book_id>',views.remove_from_cart, name='removefromcart'),
]