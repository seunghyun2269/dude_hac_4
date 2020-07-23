<<<<<<< HEAD

=======
>>>>>>> 79557d130f8ff2f240861051f55612e8b0b1f24e
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
<<<<<<< HEAD
]
=======
]
>>>>>>> 79557d130f8ff2f240861051f55612e8b0b1f24e
