from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='bookstore-home'),
    path('cart', views.cart_home, name='cart'),
]