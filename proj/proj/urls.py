<<<<<<< HEAD

=======
>>>>>>> 79557d130f8ff2f240861051f55612e8b0b1f24e
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.login, name='login'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('post.urls')),
<<<<<<< HEAD
]
=======
]
>>>>>>> 79557d130f8ff2f240861051f55612e8b0b1f24e
