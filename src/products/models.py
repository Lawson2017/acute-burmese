from django.db import models

# Create your models here.
# how to map to the data base
# any time you make changes to models.py and settings.py, you must run makemigrations and migrate to map it to the database.
class Product (models.Model):
	title 		 = models.CharField(max_length=120) # max_length = required
	description  = models.TextField(blank=True, null=True)
	price		 = models.DecimalField(decimal_places=2, max_digits=10000)
	summary		 = models.TextField(blank=False, null=False)
	featured	 = models.BooleanField() 

