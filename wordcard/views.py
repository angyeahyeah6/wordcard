from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate


def index(request):
    return render(request,"index.html",locals())