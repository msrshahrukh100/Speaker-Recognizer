# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserInfo, Temp
from cpu.script import main, classify
# Create your views here.

def homepage(request) :
	return render(request, "index.html", {})


def signup(request) :
	if request.method == "POST" :
		if UserInfo.objects.filter(name=request.POST.get('name')).exists() :
			messages.error(request, "This user name already exists")
		else :
			o, created = UserInfo.objects.get_or_create(name=request.POST.get('name'), voice=request.FILES['voice'])
			main()
			messages.success(request, 'Successfully signed up!')

	return redirect("processor:homepage")


def login(request) :
	if request.method == "POST" :
		if UserInfo.objects.filter(name=request.POST.get('name')).exists() :
			t = Temp.objects.create(name=request.POST.get('name'), voice=request.FILES.get('voice'))
			result = classify(t.voice.path)
			predicted_name = result[2][int(result[0])]
			if predicted_name == request.POST.get('name') :
				messages.success(request, 'Login credentials match! Logged in as ' + request.POST.get('name'))
			else :
				messages.error(request, 'Mismatched login credentials. Please try again')

			t.delete()
		else :
			messages.error(request, "This user name does not exists")
	return render(request, "login.html", {})