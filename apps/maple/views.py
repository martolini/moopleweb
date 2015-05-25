from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from .models import Accounts

def index(request):
	u = auth.authenticate(username='martin', password='martin')
	return HttpResponse("Yes, sir.")