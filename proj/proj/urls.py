from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.login, name='login'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('post.urls')),
]