from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def login(request):
	login = 0
	if request.method == 'POST':
		enter_name = request.POST['name']
		enter_password = request.POST['password']
		user = User.objects.get(name=enter_name)
		if user is None:
			message = "使用者不存在"
		else:
			true_password = user.password
			if enter_password == true_password:
				user.login = 1
				login = user.login
				return redirect("../../word")
	return render(request,'login.html',locals())

def register(request):
	if request.method == 'POST':
		name = request.POST['name']
		password = request.POST['password']
		email = request.POST['email']
		try:
			user = User.objects.get(name=name)
		except:
			user = None
		if user is not None:
			message = '此使用者已經有人使用'
		else:
			User.objects.create(name=name, email=email, password=password)
			message = "註冊成功"
			return render(request, "login.html", locals())
	return render(request, 'register.html', locals())

