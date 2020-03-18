from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tweets.api.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('', include('auth.urls'))
]
