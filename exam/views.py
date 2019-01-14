from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from word.models import Word, Phrase, Relate, Card
from .models import Exam
import simplejson
import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/register/')
def exam(request):
	all_exam = Exam.objects.all()
	if "create_exam" in request.POST:
		name = request.POST['exam_name']
		mytype = request.POST['exam_type']
		language = request.POST['exam_lan']
		try:
			Exam.objects.get(name=name)
		except:
			Exam.objects.create(name=name,exam_type=mytype,language=language)
	return render(request,"exam.html",locals())



