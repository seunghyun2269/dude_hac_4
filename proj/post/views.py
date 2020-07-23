
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from accounts.models import Signup
# Create your views here.

def home(request):
    if request.method = "POST":
        search = request.POST["search"]
        post_list = Post.objects.filter(title__contains = search)
        return render(request, 'result.html', {'result' : post_list})
    else:
        post_list = Post.objects.all()
        return render(request, 'home.html', {'result' : post_list})

def detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'detail.html', {'post' : post})

def profile(request, id):

