from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from .models import Word

# Create your views here.
def index(request):
	
    return render(request,"index.html",locals())