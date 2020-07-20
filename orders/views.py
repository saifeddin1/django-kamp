from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from carts.models import Cart
from .utils import send_success_email


# def address(request):
#     customer = request.user.customer
#     return render(request, 'orders/address.html', {'customer': customer})


def place_order(request):
    user = request.user
    cart = user.cart

    order = Order.objects.create(user=user)
    for item in cart.items.all():
        order.items.add(item)
    if request.method == 'POST':

        order.address = request.POST['final_address']
        order.save()
        send_success_email(request, user, order)
        return render(request, 'orders/order_success.html')
    return render(request, 'orders/order.html', {'customer': user.customer})
