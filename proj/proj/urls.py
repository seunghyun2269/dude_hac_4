from django.contrib import admin
from django.urls import path
from accounts import views
# media
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('post.urls')),
]