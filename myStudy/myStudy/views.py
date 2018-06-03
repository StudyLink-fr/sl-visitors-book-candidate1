from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from django.views.generic import View

def index(request):
	return render(request, 'homepage.html')
