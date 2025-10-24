"""URL configuration for the catalog app."""

from django.urls import path
from .views import (
    HomeView,
    AddWorkerView,
    AddPositionView,
    AddTaskTypeView,
    AddTaskView,
    TaskListView,
    TaskDetailView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-worker/", AddWorkerView.as_view(), name="add_worker"),
    path("add-position/", AddPositionView.as_view(), name="add_position"),
    path("add-task-type/", AddTaskTypeView.as_view(), name="add_task_type"),
    path("add-task/", AddTaskView.as_view(), name="add_task"),
    path("tasks-list/", TaskListView.as_view(), name="tasks"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
]
