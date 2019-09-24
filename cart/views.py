from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .models import Cart
from bookstore.models import Book

def cart_home(request):
   
    if 'my_cart' not in request.session:
        context = {"emptycart": True}
    else:
        my_cart_id = request.session['my_cart']
        cart_obj = Cart.objects.get(id=my_cart_id)
        if cart_obj.items.count() == 0:
            context = {"emptycart": True}
        else: 
            total = 0
            for item in cart_obj.items.all():
                total = total + item.price    #price is name under product model
                cart_obj.total = total
            context= {"nonemptycart": cart_obj}

    return render(request, 'carthome.html',context) #getting it from db


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

    #book = Product.get(id)
    cart.items.add(book)

    cart.save()
    #return redirect('producthome')     #needs to redirect to individual product detail page!!!!!!
    
    return redirect(request.GET.get('from'))

def remove_from_cart(request, book_id):
    my_cart_id = request.session['my_cart']
    cart= Cart.objects.get(id=my_cart_id)
    book = Book.objects.get(id=book_id)
    cart.items.remove(book)
    cart.save()
    return redirect('cart') 
