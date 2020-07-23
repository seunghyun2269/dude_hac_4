from django.conf.urls import url
from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name="home"),
    path('profile/<int:id>',views.profile, name="profile"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('delete', views.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)