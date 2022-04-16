from email import message

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'home.html')
def loginview(request):
    if request.method == 'POST':
        username=request.post.get('uname')
        password=request.post.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminhome')
            elif user.is_student:
                return redirect('studenthome')
        else:
            message.info(request,'invalid credentials')
    return render(request, 'login.html')
def adminview(request):
    return render(request,'adminhome.html')
def studentview(request):
    return render(request,'studenthome.html')

