from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    # @property
    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
    instance.cart.save()
