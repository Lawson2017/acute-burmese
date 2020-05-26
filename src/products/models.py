from django.db import models

# Create your models here.
# how to map to the data base
# any time you make changes to models.py and settings.py, you must run makemigrations and migrate to map it to the database.
class Product (models.Model):
	title 		 = models.TextField()
	description  = models.TextField()
	price		 = models.TextField()
	summary		 = models.TextField(default = 'this is cool!')

