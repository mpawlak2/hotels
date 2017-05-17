from django.db import models

# Create your models here.

class Hotel(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=40)
	price = models.DecimalField(max_digits=8, decimal_places=2)