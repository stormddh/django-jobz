from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=100)
	contact = models.CharField(max_length=50)

class Offer(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	location = models.CharField(max_length=50)
	offer_title = models.CharField(max_length=50)
	offer_text = models.CharField(max_length=200)
