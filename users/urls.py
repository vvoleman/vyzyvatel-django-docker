from django.urls import path
from .views import Authentication

urlpatterns = [
    path('authentication/', Authentication),
]
