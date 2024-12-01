from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Login', views.Login, name='Login'),
    path('Comprador/', views.Comprador, name='Comprador'),
    path('Vendedor/', views.Vendedor, name='Vendedor'),
]