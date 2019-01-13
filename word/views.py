from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from .models import Word, Phrase, Relate, Card
import simplejson
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/account/register/')
def index(request):
	relate = []
	if "create_word" in request.POST:
		word = request.POST['word_name']
		definition = request.POST['word_def']
		Word.objects.create(name=word, definition=definition)
	all_word = Word.objects.all()
	for i in all_word:
		try:
			relate_array = []
			get_relate = Relate.objects.filter(word=i)
			for  j in get_relate:
				relate_array.append(j.phrase.name)
		except:
			relate_array = []
		relate.append(relate_array)
	print(relate) #array of array
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
		print(word_relate)
		for i in word_relate:
			if len(i) >= 4:
				try:
					word = Word.objects.get(name=i)
				except:
					Word.objects.create(name=i)
					word = Word.objects.get(name=i)
				Relate.objects.create(word=word,phrase=phrase)
	all_phrase = Phrase.objects.all()
	phrases = []
	definition_p = []
	for i in all_phrase:
		phrases.append(i.name)
		definition_p.append(i.phraseDef)

	return render(request,"phrase.html",locals())
def card(request):
	message = ""
	all_word = []
	# all_card = Card.objects.all()
	if "find_card" in request.POST:
		card_name = request.POST["card_name"]
		print(card_name)
		try: 
			all_word = Card.objects.filter(name=card_name).word
			message = "find it"
		except:
			message = "Can't find the card, dude."
	return render(request,"card.html",locals())




