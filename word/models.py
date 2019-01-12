from django.db import models
from django.utils.timezone import now
from django.contrib import admin
from django.conf import settings
# Create your models here.
	




class Word(models.Model):
	name = models.CharField(max_length=64,blank = True)
	definition = models.CharField(max_length=64,blank = True)

	def __str__(self):
		return self.name
class Phrase(models.Model):
	name = models.CharField(max_length=64,blank = True)
	phraseDef = models.CharField(max_length=64,blank = True)

class Relate(models.Model):
	word = models.ForeignKey(Word, on_delete=models.CASCADE, blank = False)
	phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE,blank = False)



		
