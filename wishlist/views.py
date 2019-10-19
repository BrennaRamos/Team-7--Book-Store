from django.shortcuts import render, redirect
from django.views.generic import ListView
from bookstore.models import Book
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

def add_wish(request, book_id, homeNum):

    theBook = Book.objects.get(id = book_id)
    newEnt = WishlistEntrie(username = request.user.username, book = theBook, home = homeNum )
    newEnt.save()

    return redirect(request.GET.get('from'))
