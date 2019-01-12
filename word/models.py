from django.db import models
from django.utils.timezone import now
from django.contrib import admin
from django.conf import settings
# Create your models here.
class Word(models.Model):
	name = models.CharField(max_length=64,blank = True)
class Category(models.Model):
	catDef = models.CharField(max_length=64,blank = True)
	word = models.OneToOneField(Word,on_delete=models.CASCADE,primary_key=True)


	

	def __str__(self):
		return self.name
class Phrase(models.Model):
	phraseDef = models.CharField(max_length=64,blank = True)



		