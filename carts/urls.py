from django.urls import path
from .views import add_to_cart, remove_from_cart, cart, empty_cart


urlpatterns = [
    path('', cart, name="cart"),
    path('add/<product_id>/', add_to_cart, name="add_to_cart"),
    path('remove/<product_id>/', remove_from_cart, name="remove_from_cart"),
    path('empty-cart/', empty_cart, name="empty_cart"),

]
