from django.shortcuts import render
from .models import Task

def home(request):
    return render(request, 'home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
