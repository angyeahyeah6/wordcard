from django.db import models

# Create your models here.

class User(models.Model):
	"""docstring for User"""
	name = models.CharField(max_length=64,blank = True)
	password = models.CharField(max_length=64,blank = True)
	email = models.EmailField(max_length=64,blank = True)
	login = 0
		