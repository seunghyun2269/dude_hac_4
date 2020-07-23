from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Signup

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password=request.POST['password1'])
            signup = Signup()
            signup.user = user
            signup.address = request.POST['address']
            signup.college = request.POST['college']
            signup.save()
            auth.login(request, user)
            return redirect('/')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    