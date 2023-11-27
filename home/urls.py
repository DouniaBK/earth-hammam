from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hammam', views.hammam, name='hammam'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
]
