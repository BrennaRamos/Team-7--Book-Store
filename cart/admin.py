from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem, SaveForLater

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(SaveForLater)