
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from accounts.models import Signup
# Create your views here.

def home(request):
    if request.method = "POST":
        search = request.POST["search"]
        post_list = Post.objects.filter(title = search)
    else:
        post_list = Post.objects.all()

