from django.db import models
from django.apps import apps

# Create your models here.
class WishlistName(models.Model):
    username = models.CharField(max_length=150, help_text='Username here',  primary_key=True)
    wish_list_name_0 = models.CharField(max_length=20, help_text='Enter name for wishlist', default='Wishlist')
    wish_list_name_1 = models.CharField(max_length=20, help_text='Enter name for wishlist', null=True, blank=True)
    wish_list_name_2 = models.CharField(max_length=20, help_text='Enter name for wishlist', null=True, blank=True)


    def __str__(self):
        return self.username + '\'s Wishlists: ' 

class WishlistEntrie(models.Model):
    username = models.CharField(max_length=150, help_text='Username here')
    book = models.ForeignKey('bookstore.Book', on_delete=models.SET_NULL, null=True) 
    WISHLIST_HOME = (('0', 'Wishlist 0'), ('1', 'Wishlist 1'), ('2', 'Wishlist 2'))
    home = models.CharField(max_length=1, choices=WISHLIST_HOME, help_text='Select a list to move book to new list')
    
    def __str__(self):
        return self.username + ' : ' +self.book.title + ' : ' + self.home
