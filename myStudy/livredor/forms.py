from django.contrib.auth.models import User
from django import forms
from .models import Message

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ['message_title', 'message_text', 'signature']
