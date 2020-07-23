from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from accounts.models import Signup
from django.contrib.auth.models import User
# Create your views here.

def home(request): # 전체 게시물을 보여줌, 만약 검색하면 해당 게시물들만 보여줌
    if request.method == "POST":
        search = request.POST["search"]
        post_list = Post.objects.filter(title__contains = search)
        return render(request, 'result.html', {'result' : post_list})
    else:
        post_list = Post.objects.all()
        return render(request, 'home.html', {'result' : post_list})

def detail(request, id): # home -> detail / 게시물 세부 사항 보여줌, 댓글 작성 가능
    post = Post.objects.get(id = id)
    if request.method == "POST":
        comment = Comment()
        user = request.user
        comment.post = post
        comment.user = user
        comment.body = request.POST["comment"]
        comment.pub_date = timezone.datetime.now()
        comment.save()
        redirect('detail', id = post.id)
    return render(request, 'detail.html', {'post' : post})

def profile(request, id): # detail or home -> profile / 유저 프로필, 평점 먹일 수 있음
    post = Post.objects.get(id = id)
    profile = Signup.objects.get(user = post.user)
    if request.method == "POST":
        profile.grade = request.POST['grade']
        profile.comment = request.POST['comment']
        profile.save()
        return redirect('profile', id = post.id)
    return render(request, 'profile.html', {'profile' : profile})

def create(request): # 게시물 생성
    if request.method == "POST":
        post = Post()
        user = request.user
        post.user = user
        post.title = request.POST['title']
        post.image = request.FILES['image']
        post.pub_date = timezone.datetime.now()
        post.body = request.POST['body']
        post.save()
        return redirect('home')
    return render(request, 'create.html')
    

def delete(request, id): # 게시물 삭제
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('home')
