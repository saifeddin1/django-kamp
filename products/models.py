from django.db import models
from django.urls import reverse


class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)

	def get_absolute_url(self):
		return reverse('product-details', args=(self.id,))

	def __str__(self):
		return self.title