from django.urls import path
from .views import *


urlpatterns = [
    path('products/', product_list, name="product-list"),
    path('products/<pk>/', product_details, name="product-details"),
]
