from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from accounts.models import Signup
# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
