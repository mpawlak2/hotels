from django.db import models

class HotelModel(models.Model):
	name = models.CharField(max_length=50, verbose_name='Hotel name:')
	slug = models.SlugField(max_length=40)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.TextField(null=True, blank=True)



	class Meta:
		verbose_name = 'Hotel'
		verbose_name_plural = 'Hotels'

	def __str__(self):
		return self.name