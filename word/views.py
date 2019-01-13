from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from .models import Word, Phrase, Relate
import simplejson
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/register/')
def index(request):
	if "create_word" in request.POST:
		word = request.POST['word_name']
		definition = request.POST['word_def']
		Word.objects.create(name=word, definition=definition)
	all_word = Word.objects.all()
	word = []
	definition = []
	for i in all_word:
		word.append(i.name)
		definition.append(i.definition)
	return render(request,"index.html",locals())
@login_required(login_url='/account/register/')
def phrase(request):
	word_relate = []
	phrases = ""
	if "create_phrase" in request.POST:
		phrases = request.POST['phrase_name']
		definition = request.POST['phrase_def']
		phrase = Phrase.objects.create(name=phrases, phraseDef=definition)
		word_relate = phrases.split(" ")
		for i in word_relate:
			if len(i) > 5:
				try:
					word = Word.objects.get(name=i)
				except:
					word = Word.objects.create(name=i,definition="")
				Relate.objects.create(word=word,phrase=phrase)
	all_phrase = Phrase.objects.all()
	phrases = []
	definition = []
	for i in all_phrase:
		phrases.append(i.name)
		definition.append(i.phraseDef)

	return render(request,"phrase.html",locals())
