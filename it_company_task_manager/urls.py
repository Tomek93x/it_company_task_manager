"""URL configuration for the IT Company Task Manager project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
]
