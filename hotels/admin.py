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
			'age',
			'active',
	]

	readonly_fields = [
		'slug',
		'insert_date',
		'updated',
		'timestamp',
		'age', 
	]

	def age(self, obj, *args, **kwargs):
		return str(obj.age)

	class Meta:
		model = HotelModel


admin.site.register(HotelModel, HotelModelAdmin)