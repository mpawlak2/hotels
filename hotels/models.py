from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
HOTEL_STARS = [
		('1', 'One star hotel.'),
		('2', 'Two stars hotel.'),
		('3', 'Three stars hotel.'),
		('4', 'Four stars hotel.'),
		('5', 'Five stars hotel.'),
	]

class HotelModel(models.Model):
	name 			= models.CharField(max_length=50, verbose_name='Hotel name')
	slug 			= models.SlugField(max_length=40, unique=True, null=True, blank=True, error_messages={'unique': 'This slug is not unique.'})
	price 			= models.DecimalField(max_digits=8, decimal_places=2)
	description 	= models.TextField(null=True, blank=True)
	stars 			= models.CharField(max_length=1, verbose_name='Hotel stars', choices=HOTEL_STARS, default='1')
	insert_date		= models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Hotel'
		verbose_name_plural = 'Hotels'

	def __str__(self):
		return self.name


def hotel_model_pre_save(sender, instance, *args, **kwargs):
	if not instance.slug and instance.name:
		instance.slug = slugify(instance.name)

pre_save.connect(hotel_model_pre_save, sender=HotelModel)