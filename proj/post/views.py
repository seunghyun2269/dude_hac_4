from django.shortcuts import render,get_object_or_404

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
