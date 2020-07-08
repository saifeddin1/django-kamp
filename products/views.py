from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddProductForm


def product_list(request):
	products = Product.objects.all()
	return render(request, 'products/products.html', {'products':products})


def product_details(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'products/product_detail.html', {'product':product})


def product_add(request):
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'products/product-add-successful.html')
	else:
		
		form = AddProductForm()

	return render(request, 'products/product-add.html', {'form':form})


def product_edit(request, pk):
	product = get_object_or_404(Product, pk=pk)

	if request.method == 'POST':
		form = AddProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return render(request, 'products/product-add-successful.html')
	else:
		
		form = AddProductForm(instance=product)

	return render(request, 'products/product-add.html', {'form':form})


def product_delete(request, pk):
	product = get_object_or_404(Product, pk=pk)
	product.delete()
	return redirect('product-list')