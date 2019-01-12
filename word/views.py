from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from .models import Word, Phrase
import simplejson
import json


# Create your views here.
def index(request):
	if "create_word" in request.POST:
		word = request.POST['word_name']
		definition = request.POST['word_def']
		Word.objects.create(name=word, definition=definition)
	all_word = Word.objects.all()
	word = []
	defi = []
	for i in all_word:
		word.append(i.name)
		defi.append(i.definition)

	return render(request,"index.html",locals())

def phrase(request):
	if "create_phrase" in request.POST:
		phrases = request.POST['phrase_name']
		definition = request.POST['phrase_def']
		Phrase.objects.create(name=phrases, phraseDef=definition)
	all_phrase = Phrase.objects.all()
	return render(request,"phrase.html",locals())
