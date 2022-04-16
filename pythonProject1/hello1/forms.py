from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(UserCreationForm):
   # Username = forms.CharField()
   # Password = forms.CharField()
    class Meta:
        model = Login
        exclude = ('Last name','Password')
class EmailForm(forms.ModelForm):
      class Meta:
          model = Email
          # fields=('Email','Phone')
          exclude = ('Email',)