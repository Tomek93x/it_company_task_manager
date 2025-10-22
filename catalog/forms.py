from django import forms
from .models import Position, Worker, Task, TaskType


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'position', 'password'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name', 'description', 'deadline', 'priority',
            'task_type', 'assignees'
        ]
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
