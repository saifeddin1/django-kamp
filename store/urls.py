from django.contrib import admin
from django.urls import path
from products.views import say_hi, show_time
urlpatterns = [
    path('admin/', admin.site.urls),
    path('say-hi/<str:name>', say_hi),
    path('show-time', show_time),
]
