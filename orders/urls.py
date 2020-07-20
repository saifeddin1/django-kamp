from django.urls import path, include
from .views import *

urlpatterns = [
    path('orders/place_order/', place_order, name='place_order'),
]
