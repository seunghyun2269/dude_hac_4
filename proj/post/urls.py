from django.conf.urls import url
from django.urls import path
from post import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('profile/<int:id>',views.profile, name="profile"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('delete', viwes.delete, name="delete"),
]