from django.shortcuts import render
from django.views.generic import ListView
from wishlist.models import WishlistName, WishlistEntrie
from wishlist.forms import WishlistNameForm

# Create your views here.

def wishlist(request):
    return render(request, 'wishlist/home.html')

class WishlistNameList(ListView):
    model = WishlistName

    def entries(self):
        return WishlistEntrie.objects.all()

def rename_wish(request):
    wish_names_instance = get_object_or_404(WishlistName, pk=1)
    if request.method == 'POST':
        form = WishlistNameForm(request.POST)
        wish_names_instance.wish_list_name_0 = request.POST['wishlist_1']
        wish_names_instance.wish_list_name_1 = request.POST['wishlist_2']
        wish_names_instance.wish_list_name_2 = request.POST['wishlist_3']
        return HttpResponseRedirect('wishlist/home.html')

    else:
        form = WishlistNameForm()
        
    
    return render(request, 'wishlist/home.html', {'form' : form})
