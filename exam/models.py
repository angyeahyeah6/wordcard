from django.db import models

# Create your models here.
from datetime import datetime


class Exam(models.Model):
	name = models.CharField(max_length=64,blank = True)
	exam_type = models.CharField(max_length=64,blank = True)
	language = models.CharField(max_length=64,blank = True)
	taken_people = models.IntegerField(default = 0)
	level = models.IntegerField(default = 0)

	def __str__(self):
		return self.name
