from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from carts.models import Cart
from .utils import send_success_email
from django.template.loader import render_to_string


def address(request):
    customer = request.user.customer
    return render(request, 'orders/address.html', {'customer': customer})


def complete_order(request):
    user = request.user
    cart = user.cart
    order = Order.objects.create(user=user)
    for item in cart.items.all():
        order.items.add(item)
    order.address = request.POST['final_address']
    order.save()

    subject = 'Order Successfuly Placed'
    context = {'user': user, 'order': order}
    message = render_to_string(
        'orders/success_email.html', context)

    user.email_user(subject, message)
    # send_success_email(request, user, order)
    return render(request, 'orders/order_success.html')
