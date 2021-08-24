from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from simplemathcaptcha.fields import MathCaptchaField

class SignUpForm(UserCreationForm):
	captcha = MathCaptchaField()
	class Meta:
		model = User
		fields = ('username','password1','password2','captcha')