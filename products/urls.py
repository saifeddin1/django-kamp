from django.urls import path
from .cbviews import *


urlpatterns = [
    path('products/', ProductList.as_view(), name="product-list"),
    path('products/add/', ProductAdd.as_view(), name="product-add"),
    path('products/<int:pk>/', ProductDetail.as_view(), name="product-details"),
    path('products/edit/<int:pk>/', ProductEdit.as_view(), name="product-edit"),
    path('products/delete/<int:pk>/',
         ProductDelete.as_view(), name="product-delete"),

    # path('products/', product_list, name="product-list"),
    # path('products/add/', product_add, name="product-add"),
    # path('products/<pk>/', product_details, name="product-details"),
    # path('products/edit/<pk>/', product_edit, name="product-edit"),
    # path('products/delete/<pk>/', product_delete, name="product-delete"),
]
