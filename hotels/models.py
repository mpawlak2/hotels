from django.db import models

class HotelModel(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=40)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.TextField(null=True, blank=True)