from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='bookstore-home'),
    path('cart', views.cart_home, name='cart'),
    path('addtocart/<int:book_id>',views.add_to_cart, name='addtocart'),
    path('removefromcart/<int:book_id>',views.remove_from_cart, name='removefromcart'),
    path('addbutton/<int:book_id>',views.add_button, name='addbutton'),
    path('removebutton/<int:book_id>',views.remove_button, name='removebutton'),
    path('purchaseitems/',views.purchase_items, name='purchaseitems'),
]