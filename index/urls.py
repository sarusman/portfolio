from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('btc/', views.btc, name='btc'),
    path('license/', views.license, name='license'),
]
