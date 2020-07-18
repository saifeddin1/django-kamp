from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import Customer
from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    # customer_address = models.ForeignKey(
    #     Customer, to_field='address', null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
