<<<<<<< HEAD
from django.shortcuts import render,get_object_or_404

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
=======
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from accounts.models import Signup
# Create your views here.

def main()
>>>>>>> b1985b34ad254adc5855ae64d6abd267a0430cd8
