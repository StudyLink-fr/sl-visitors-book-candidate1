from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Message
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, MessageForm

def index(request):
	model = Message
	user = request.user
	latest_message_list = Message.objects.all().order_by('-id')[:10]
	return render(request, 'livredor/index.html', {'latest_message_list': latest_message_list, 'user': user})

def delete_message(request, pk):
	message = get_object_or_404(Message, pk=pk)
	message.delete()
	latest_message_list = Message.objects.all().order_by('-id')[:10]
	return render(request, 'livredor/index.html', {'latest_message_list': latest_message_list})

def detail(request, pk):
	message = get_object_or_404(Message, pk=pk)
	return render(request, 'livredor/detail.html', {'message': message})

def create_message(request):
	if not request.user.is_authenticated():
		return render(request, 'livredor/login.html')
	else:
		form = MessageForm(request.POST or None)
		if form.is_valid():
			message = form.save(commit=False)
			message.user = request.user
			message.save()
			return render(request, 'livredor/detail.html', {'message': message})
		else:
			return render(request, 'livredor/message_form.html', {'form': form})

class UserFormView(View):
	form_class = UserForm
	template_name = 'livredor/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('livredor:index')

		return render(request, self.template_name, {'form': form})

def logout_user(request):
	logout(request)
	model = Message
	latest_message_list = Message.objects.all().order_by('-id')[:10]
	return render(request, 'livredor/index.html', {'latest_message_list': latest_message_list})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				model = Message
				latest_message_list = Message.objects.all().order_by('-id')[:10]
				return render(request, 'livredor/index.html', {'latest_message_list': latest_message_list})
			else:
				return render(request, 'livredor/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'livredor/login.html', {'error_message': 'Invalid login'})
	return render(request, 'livredor/login.html')
