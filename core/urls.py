from django.urls import path
from .views import home, download_apk

urlpatterns = [
    path('', home, name="home")
]
