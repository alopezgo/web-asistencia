from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('descargar/', views.download_apk, name='download_apk'),
]
