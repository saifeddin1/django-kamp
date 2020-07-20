from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.contrib.auth.decorators import login_required

from .utils import send_success_email
from.forms import OrderForm


@login_required
def place_order(request):
    user = request.user

    if not user.cart.items.exists():
        return redirect('product-list')

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():

            order = form.save(user)
            order.address = form.cleaned_data['address']
            order.save()
            send_success_email(request, user, order)
            return render(request, 'orders/order_success.html')
    else:
        form = OrderForm()

    context = {'customer': user.customer, 'form': form}
    return render(request, 'orders/order.html', context)
