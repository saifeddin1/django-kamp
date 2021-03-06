from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.remove(product)

    return redirect('cart')


def empty_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.items.clear()
    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    cart = user.cart
    products = cart.items.all()
    # total_price = user.cart.total_price()
    total_price = cart.items.aggregate(
        total_price=Sum('price'))['total_price']
    context = {'products': products, 'total_price': total_price, 'cart': cart}

    return render(request, 'carts/cart.html', context)
