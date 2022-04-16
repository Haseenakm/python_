import LoginForm as LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'index.html')


class LoginForm:
    pass


def signin(request):
    form = LoginForm()
    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
             login(request,user)
             if user.is_staff:
               return redirect('index')
              else:
                return redirect('index')
        else:
            messages.error(request,'invalid credentials')
            return redirect('signin')
    return render(request,'login.html',{'form'})