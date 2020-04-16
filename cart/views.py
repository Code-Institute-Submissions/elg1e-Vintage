from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """
    View what is inside the cart
    """
    return render(request, "cart.html")

def add_to_cart(request, id):
    """
    Add items to cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {}) 
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))

def adjust_cart(request):
    """
    adjust the quantity of cart items
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session(reverse('view_cart')) 