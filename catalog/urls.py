"""URL configuration for catalog app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-worker/', views.add_worker, name='add_worker'),
    path('add-position/', views.add_position, name='add_position'),
    path('add-task/', views.add_task, name='add_task'),
    path('tasks/', views.task_list, name='task_list'),
]
