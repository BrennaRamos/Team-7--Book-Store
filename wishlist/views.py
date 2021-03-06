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
    wish_names_instance = WishlistName.objects.all().filter(username = request.user).first()
    if wish_names_instance:
        form = WishlistNameForm(request.POST or None, initial={'wish_list_name_0': wish_names_instance.wish_list_name_0, 'wish_list_name_1': wish_names_instance.wish_list_name_1, 'wish_list_name_2': wish_names_instance.wish_list_name_2})

    if not wish_names_instance:
        newNames = WishlistName(username = request.user.username)
        newNames.save()
        wish_names_instance = newNames
        form = WishlistNameForm(request.POST or None, initial={'wish_list_name_0': wish_names_instance.wish_list_name_0, 'wish_list_name_1': wish_names_instance.wish_list_name_1, 'wish_list_name_2': wish_names_instance.wish_list_name_2})

    if request.method == 'POST':
        if form.is_valid():
            wish_names_instance.wish_list_name_0 = request.POST.get('wish_list_name_0')
            wish_names_instance.wish_list_name_1 = request.POST.get('wish_list_name_1')
            wish_names_instance.wish_list_name_2 = request.POST.get('wish_list_name_2')
            wish_names_instance.save()
        return redirect('wishlists')

    else:
        form = WishlistNameForm(instance = wish_names_instance)

    context = {
        'WishlistNameForm':form,
        'wish_names_instance':wish_names_instance
    }
        
    
    return render(request, 'wishlist/home.html', context)

def add_wish(request, book_id, homeNum):

    theBook = Book.objects.get(id = book_id)
    newEnt = WishlistEntrie(username = request.user.username, book = theBook, home = homeNum )
    newEnt.save()

    return redirect(request.GET.get('from'))

def trans_wish(request, entrie_id, newHome):

    oldEntrie = WishlistEntrie.objects.get(id = entrie_id)
    newEntrie = WishlistEntrie(username = oldEntrie.username, book = oldEntrie.book, home = newHome )
    oldEntrie.delete()
    newEntrie.save()
    return redirect(request.GET.get('from'))

def del_wish(request, entrie_id):
    
    trashEntrie = WishlistEntrie.objects.get(id = entrie_id)
    trashEntrie.delete()
    return redirect(request.GET.get('from'))
        
