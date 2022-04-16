from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from saloonapp.forms import *


# Create your views here.
def home(request):
    return render(request, 'index.html')


def signin(request):
    # form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            Login(request,user)
            if user.is_staff:
                return redirect('Admin_Home')
            else:
                return redirect('User_Home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('signin')
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def Admin_Home(request):
    return render(request, 'Admin_Home.html')


def User_Home(request):
    return render(request, 'User_Home.html')
