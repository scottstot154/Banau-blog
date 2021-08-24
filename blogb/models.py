from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to="images/")
	description = models.TextField()
	private = models.BooleanField(default=False)

	def __str__(self):
		return self.description + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('home')