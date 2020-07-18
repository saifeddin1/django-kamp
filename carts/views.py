from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart
from django.contrib.auth.decorators import login_required


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
    cart.items.all().delete()
    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()
    context = {'products': products}

    return render(request, 'carts/cart.html', context)
