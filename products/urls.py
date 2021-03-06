from django.urls import path
from .views import *


urlpatterns = [
    path('products/', product_list, name="product-list"),
    path('products/add/', product_add, name="product-add"),
    path('products/<int:pk>/', product_details, name="product-details"),
    path('products/edit/<int:pk>/', product_edit, name="product-edit"),
    path('products/delete/<int:pk>/', product_delete, name="product-delete"),

]
