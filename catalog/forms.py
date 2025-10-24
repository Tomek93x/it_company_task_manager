import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Position, Worker, Task, TaskType, TaskComment


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ['name']


class WorkerForm(forms.ModelForm):
    username = forms.CharField(
        max_length=16
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text=(
            "Password must be at least 8 characters long, "
            "contain an uppercase letter, a lowercase letter, and a digit."
        )
    )

    class Meta:
        model = Worker
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'position', 'password'
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError(
                "Password must be at least 8 characters long."
            )
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                "Password must contain at least one lowercase letter."
            )
        if not re.search(r'\d', password):
            raise ValidationError(
                "Password must contain at least one digit."
            )
        return password


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


class TaskCommentForm(forms.ModelForm):

    class Meta:
        model = TaskComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 2,
                    'class': 'form-control',
                    'placeholder': 'Enter your comment'
                }
            ),
        }
