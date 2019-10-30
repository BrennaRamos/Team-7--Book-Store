from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .models import Cart, CartItem, SaveForLater
from bookstore.models import Book, Book_User
from django.contrib.auth.models import User

def cart_home(request):
   
    if 'my_cart' not in request.session:
        context = {"emptycart": True}
    else:
        my_cart_id = request.session['my_cart']
        cart_obj = Cart.objects.get(id=my_cart_id)
        qs2 = SaveForLater.objects.get(cart=cart_obj)
        if cart_obj.items.count() == 0:
            cart_obj.total = 0.00
            #qs2 = SaveForLater.objects.get(cart=cart_obj)
            if qs2.items.count() == 0:
                context = {"emptycart": True, "notsaveforlater": True}
            else:
                context = {"emptycart": True, "saveforlater": qs2}
        else: 
            total = 0
            for item in cart_obj.items.all():
                cart_item_quantity = CartItem.objects.get(cart=cart_obj, book=item)
                cart_item_quantity.quantityprice = item.price * cart_item_quantity.quantity
                cart_item_quantity.save()
                total = total + cart_item_quantity.quantityprice    #price is name under product model
                cart_obj.total = total
                cart_obj.save()

            qs = CartItem.objects.all()
            #qs2 = SaveForLater.objects.get(cart=cart_obj)
            if qs2.items.count() == 0:
                context= {"nonemptycart": cart_obj, "cartitem": qs, "notsaveforlater": True}
            else:
                context= {"nonemptycart": cart_obj, "cartitem": qs, "saveforlater": qs2}

    return render(request, 'carthome.html',context) #getting it from db

def add_button(request, book_id):
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id)
    cart_item_quantity = CartItem.objects.get(cart=cart, book=book_id)
    if cart_item_quantity.quantity < 10:
        cart_item_quantity.quantity += 1
        cart_item_quantity.save()
    else:
        cart_item_quantity.quantity = 10
    cart_item_quantity.save()

    return redirect('cart') 

def remove_button(request, book_id):
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id)
    cart_item_quantity = CartItem.objects.get(cart=cart, book=book_id)
    if cart_item_quantity.quantity > 1:
        cart_item_quantity.quantity -= 1
        cart_item_quantity.save()
    else:
        cart_item_quantity.delete()
        cart.items.remove(book_id)
        cart.save()     

    return redirect('cart') 

def add_to_cart(request, book_id):
    request.session.set_expiry(5000000)   
    if 'my_cart' not in request.session:
        create_new_cart = Cart()
        create_new_cart.save()
        request.session['my_cart'] = create_new_cart.id
        my_cart_id = create_new_cart.id
    else:
        my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id) 
    book = Book.objects.get(id=book_id)
    cart.items.add(book)
    cart_item_quantity = CartItem.objects.get_or_create(cart=cart, book=book)
    cart.save()

    #save_for_later = SaveForLater.objects.get(cart=cart)    
    save_for_later, created = SaveForLater.objects.get_or_create(cart=cart)  
    save_for_later.items.remove(book)
    save_for_later.save()
   
    return redirect(request.GET.get('from'))

def remove_from_cart(request, book_id):
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id)
    book = Book.objects.get(id=book_id)
    cart_item_quantity = CartItem.objects.get(cart=cart, book=book)
    cart_item_quantity.delete()       
    cart.items.remove(book)
    cart.save()
    
    return redirect('cart') 

def purchase_items(request):
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id) 
    user = request.user
    for item in cart.items.all():
        book = Book.objects.get(id=item.id)
        if user.is_authenticated and not Book_User.objects.filter(book=book, user=user).exists():
            #for item in cart.items.all():
                new_user_book = Book_User.objects.create(user=user, book=book)
       # else:
        #    continue  

        cart.items.remove(book)
        cart.save()
    #del request.session['my_cart']

    
    return render(request, 'purchase.html')

def save_for_later(request, book_id):  
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id)
    book = Book.objects.get(id=book_id)
    save_for_later, created = SaveForLater.objects.get_or_create(cart=cart)
    save_for_later.items.add(book)
    save_for_later.save()
   
    #cart_item_quantity = CartItem.objects.get(cart=cart, book=book)
    #cart_item_quantity.delete()       
    cart.items.remove(book)
    cart.save()

    return redirect('cart') 

def remove_from_saveforlater(request, book_id):
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id)
    book = Book.objects.get(id=book_id)
    save_for_later = SaveForLater.objects.get(cart=cart)      
    save_for_later.items.remove(book)
    save_for_later.save()
    
    return redirect('cart')