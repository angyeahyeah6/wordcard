from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log in the user
			user = form.get_user()
			login(request,user)
			return redirect('../../word/')
		else:
			return redirect("../../word/")
	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# log the user in
			login(request,user)
			# return redirect('articles:list')
			return redirect('../../word/')
	else:
		form = UserCreationForm()
	return render(request,'register.html',{'form':form})

def logout_view(request):
	logout(request)
	return redirect('../../word/')
