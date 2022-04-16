from django.shortcuts import render
from hello1.forms import *
# Create your views here.
def index(request):
    form = LoginForm()
    return render(request,'index.html',{'form': form})
def Email(request):
    f = EmailForm()
    return render(request,'Emailsample.html',{'form': f})