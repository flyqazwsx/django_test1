from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.viewtodo, name='viewtodo'),
    path('create/', views.create_todo, name='create'),
    path('completed/', views.completed, name='completed'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('completed_by_id/<int:id>', views.completed_by_id, name='completed_by_id'),
    path('sort/', views.sorttodo, name='sort'),
]
