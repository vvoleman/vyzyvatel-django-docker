from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('users.urls')),
    path('api/', include('questions.urls')),
    path('', admin.site.urls),
]
