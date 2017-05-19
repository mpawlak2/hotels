from django.contrib import admin

# Register your models here.
from .models import HotelModel

class HotelModelAdmin(admin.ModelAdmin):
	fields = [
			'name',  		
			'price', 		
			'description',
			'stars', 		
			'slug',
			'updated',
			'insert_date',
			'timestamp',
	]

	readonly_fields = [
		'slug',
		'insert_date',
		'updated',
		'timestamp',
	]

	class Meta:
		model = HotelModel


admin.site.register(HotelModel, HotelModelAdmin)