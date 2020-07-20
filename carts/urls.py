from django.urls import path
from .views import add_to_cart, remove_from_cart, cart, empty_cart


urlpatterns = [
    path('carts/', cart, name="cart"),
    path('carts/add/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('carts/remove/<int:product_id>/',
         remove_from_cart, name="remove_from_cart"),
    path('carts/empty-cart/', empty_cart, name="empty_cart"),

]
