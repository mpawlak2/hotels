from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.utils.timesince import timesince
from datetime import datetime

HOTEL_STARS = [
		('1', 'One star hotel.'),
		('2', 'Two stars hotel.'),
		('3', 'Three stars hotel.'),
		('4', 'Four stars hotel.'),
		('5', 'Five stars hotel.'),
	]

class HotelModeQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class HotelModelManager(models.Manager):
	def get_queryset(self):
		return HotelModeQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		qs = self.get_queryset().active()
		return qs

	def get_timeframe(self, from_date, to_date):
		qs = self.get_queryset
		qs_date_from = qs.filter(timestamp__gte=from_date)
		qs_date_to = qs_date_from.filter(timestamp__lte=to_date)

		# final_qs = (qs_date_from | qs_date_to).distinct() 
		return qs_date_to
		# Assume datetime objects.

class HotelModel(models.Model):
	name 			= models.CharField(max_length=50, verbose_name='Hotel name')
	slug 			= models.SlugField(max_length=40, unique=True, null=True, blank=True, error_messages={'unique': 'This slug is not unique.'}, help_text='Must be unique.', editable=False)
	price 			= models.DecimalField(max_digits=8, decimal_places=2)
	description 	= models.TextField(null=True, blank=True)
	stars 			= models.CharField(max_length=1, verbose_name='Hotel stars', choices=HOTEL_STARS, default='1')
	insert_date		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	active 			= models.BooleanField(default=True)

	objects = HotelModelManager()

	class Meta:
		verbose_name = 'Hotel'
		verbose_name_plural = 'Hotels'

	def __str__(self):
		return self.name

	@property
	def age(self):
		return timesince(self.timestamp)


def hotel_model_pre_save(sender, instance, *args, **kwargs):
	if not instance.slug and instance.name:
		instance.slug = slugify(instance.name)

pre_save.connect(hotel_model_pre_save, sender=HotelModel)