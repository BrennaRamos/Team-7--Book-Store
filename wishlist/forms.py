from django import forms
from .models import WishlistName
    
class WishlistNameForm(forms.ModelForm):
    #wishlist_1 = forms.CharField()
    #wishlist_2 = forms.CharField()
    #wishlist_3 = forms.CharField()
    class Meta:
        model = WishlistName
        fields = ('wish_list_name_0', 'wish_list_name_1', 'wish_list_name_2')
