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
	if "change_meaning" in request.POST:
		chinese = request.POST['chinese']
		english = request.POST['english']
		change_word = Word.objects.get(name=english)
		Word.objects.filter(id=change_word.id).update(definition=chinese)
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
	card_name = ""
	# all_card = Card.objects.all()
	if "find_card" in request.POST:
		card_name = request.POST["card_name"]
		try: 
			all_word = Card.objects.filter(name=card_name)
			message = "find it"
		except:
			message = "Can't find the card, dude."
	for i in all_word:
			all_word_answer.append(i.word.definition)
			card_name = request.POST['card_name']
	if "update_times" in request.POST:
		wrong = request.POST['wrong_time'].split(",")
		test = request.POST['test_time'].split(",")
		card_n = request.POST['card_n']
		all_word = Card.objects.filter(name=card_n)
		print("wrongtime",wrong)
		state = 0
		for i in range(len(wrong)):
			wrong[i] = int(wrong[i])
			test[i] = int(test[i])
		for i in range(len(all_word)):
			print("hihihihi")
			if wrong[i] > 0: 
				Card.objects.filter(id=all_word[i].id).update(corpercent = (1-wrong[i]/test[i]))
			if test[i] > 0:
				Card.objects.filter(id=all_word[i].id).update(testtime=test[i])
	return render(request,"test.html",locals())
@login_required(login_url='/account/register/')
def card(request):
	all_word = Word.objects.all()
	check_word = []
	author = request.user
	card_name = ""
	get_card_name = Card.objects.filter(author=author).values_list('name', flat=True).distinct()
	card_corper = []
	for i in get_card_name:
		temp_word = Card.objects.filter(name=i)
		temp_score = 0
		for j in temp_word:
			temp_score += j.corpercent
		temp_score = round(temp_score/len(temp_word),2)
		card_corper.append(temp_score)
	all_thing = zip(get_card_name,card_corper)
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



