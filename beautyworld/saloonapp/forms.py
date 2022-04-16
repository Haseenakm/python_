from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LogingForm(UserCreationForm):
    # username=forms.CharField()
    # password1=forms.CharField(widget=forms.PasswordInput,label='password')
    # password2=forms.CharField(widget=forms.PasswordInput,label='Confirm password')


    class Meta:
        model = Login
        #exclude = ('password2',)
        fields = ('username','password1')