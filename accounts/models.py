from django.db import models
# from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.id} - Customer {self.user.username}'


# def create_customer_profile(sender, instance, created, ** kwargs):
#     if created:
#         Customer.objects.create(user=instance)


# post_save.connect(create_customer_profile, sender=User)
