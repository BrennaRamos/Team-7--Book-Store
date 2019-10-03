from django import forms
    
class WishlistNameForm(forms.Form):
    wishlist_1 = forms.CharField(help_text="Enter a name for your primary wishlist.", max_length = 20)
    wishlist_2 = forms.CharField(help_text="Enter a name for your 2nd wishlist.", max_length = 20, required = False)
    wishlist_3 = forms.CharField(help_text="Enter a name for your 3rd wishlist.", max_length = 20, required = False)
