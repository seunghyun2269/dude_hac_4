<<<<<<< HEAD
from django.conf.urls import url
from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/',views.signup, name="signup"),
=======
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name = "login"),
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.logout, name = "logout"),
>>>>>>> b1985b34ad254adc5855ae64d6abd267a0430cd8
]