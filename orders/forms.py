from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('address',)

    def save(self, user, address):
        self.instance.user = user
        # self.instance.address = address
        self.instance.save()

        for item in user.cart.items.all():
            self.instance.items.add(item)

        user.cart.items.clear()

        return self.instance
