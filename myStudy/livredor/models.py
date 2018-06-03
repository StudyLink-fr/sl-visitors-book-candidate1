# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Message(models.Model):
	user = models.ForeignKey(User, unique=False)
	message_title = models.CharField(max_length=100)
	message_text = models.CharField(max_length=1500)
	signature = models.CharField(max_length=50)
	def __str__(self):
		return self.message_title + " | " + self.message_text + " | " + self.signature
	def get_absolute_url(self):
		return reverse('livredor:detail', kwargs={'pk': self.pk})
