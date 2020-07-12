from django.shortcuts import render
from .models import Product
from .forms import AddProductForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductList(ListView):
    model = Product
    template_name = 'products/products-list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product-details.html'


class ProductAdd(CreateView):
    form_class = AddProductForm
    template_name = 'products/product-add.html'

    def sucess(self, request):
        return render(request, 'products/product-add-successful.html')


class ProductEdit(UpdateView):
    model = Product
    form_class = AddProductForm
    template_name = 'products/product-add.html'

    def sucess(self, request):
        return render(request, 'products/product-add-successful.html')


class ProductDelete(DeleteView):
    model = Product
    sucess_url = '/'
