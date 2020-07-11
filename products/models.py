from django.db import models
from django.urls import reverse


class Product(models.Model):
	brand = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	price = models.FloatField(null=True)
	created_at = models.DateTimeField(null=True, auto_now_add=True)
	image = models.ImageField(upload_to='products/', null=True)
	
	def get_absolute_url(self):
		return reverse('product-details', args=(self.id,))

	def __str__(self):
		return self.title