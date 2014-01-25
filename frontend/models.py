from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
	country = models.CharField(max_length=45)
	city = models.CharField(max_length=45)
	translate_from = models.CharField(max_length=45)
	translate_to = models.CharField(max_length=45)
	user = models.OneToOneField(User,unique=True)
	class Meta:
		db_table = 'profile'
	def __str__(self):  
		  return "%s's profile" % self.user  



AUTH_PROFILE_MODULE = 'frontend.Profile'