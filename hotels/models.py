from django.db import models


HOTEL_STARS = [
		('1', 'One star hotel.'),
		('2', 'Two stars hotel.'),
		('3', 'Three stars hotel.'),
		('4', 'Four stars hotel.'),
		('5', 'Five stars hotel.'),
	]

class HotelModel(models.Model):
	name 			= models.CharField(max_length=50, verbose_name='Hotel name')
	slug 			= models.SlugField(max_length=40)
	price 			= models.DecimalField(max_digits=8, decimal_places=2)
	description 	= models.TextField(null=True, blank=True)
	stars 			= models.CharField(max_length=1, verbose_name='Hotel stars', choices=HOTEL_STARS, default='1')
	insert_date		= models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name = 'Hotel'
		verbose_name_plural = 'Hotels'

	def __str__(self):
		return self.name