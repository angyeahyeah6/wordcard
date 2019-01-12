from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from .models import Word, Phrase

# Create your views here.
def index(request):
	if "create_word" in request.POST:
		word = request.POST['word_name']
		definition = request.POST['word_def']
		Word.objects.create(name=word, definition=definition)
	all_word = Word.objects.all()
	return render(request,"index.html",locals())

def phrase(request):
	if "create_word" in request.POST:
		phrases = request.POST['phrases_name']
		definition = request.POST['phrases_def']
		Phrase.objects.create(name=phrase, definition=definition)
	all_phrase = Phrase.objects.all()
	return render(request,"phrase.html",locals())