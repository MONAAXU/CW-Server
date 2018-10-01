from django.db import models


class Enquire(models.Model):
	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length=200)
	lcoation = models.CharField(max_length=200)
	phone_number = models.IntegerField(default=0)
	request = models.CharField(max_length=200)
