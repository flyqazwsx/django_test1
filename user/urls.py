from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('register/', views.user_register),
    path('', views.user_register, name='register')
]
