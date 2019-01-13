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
def test(request):
	message = ""
	all_word = []
	all_word_answer = []
	# all_card = Card.objects.all()
	if "find_card" in request.POST:
		card_name = request.POST["card_name"]
		try: 
			all_word = Card.objects.filter(name=card_name)
			message = "find it"
		except:
			message = "Can't find the card, dude."
	if "with_answer" in request.POST:
		wordid = request.POST['with_answer']
		enter_answer = request.POST["enter_answer"]
		card_name = Card.objects.get(word__id=wordid).name
		all_word = Card.objects.filter(name=card_name)
		chin_answer = Word.objects.get(id=wordid).definition
		message = "find it"
		print(enter_answer,"     ",chin_answer)
		wordid = int(wordid)
		if enter_answer == chin_answer:
			correct = 1
		else:
			correct = 2
	for i in all_word:
			all_word_answer.append(i.word.definition)
	return render(request,"test.html",locals())
def card(request):
	all_word = Word.objects.all()
	check_word = []
	author = request.user
	card_name = ""
	if "create_card" in request.POST:
		s = request.POST
		card_name = s['card_name']
		print(card_name)
		for i in all_word:
			try:
				myid = str(i.id)
				check_word.append(Word.objects.get(name=s[myid]))
			except:
				pass
		for i in check_word:
			try:
				Card.objects.get(name=card_name,word__name=i)
			except:
				Card.objects.create(name=card_name,word=i,author=author)
	return render(request,"card.html",locals())



