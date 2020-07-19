from django.urls import path, include
from .views import *

urlpatterns = [
    path('address/', address, name='address'),
    path('complete-order/', complete_order, name='complete_order'),
]
