from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Task Type'
        verbose_name_plural = 'Task Types'

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        related_name='workers',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.username


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='normal',
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.SET_NULL,
        related_name='tasks',
        null=True,
        blank=True,
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name='tasks',
        blank=True,
    )

    class Meta:
        ordering = ['deadline', 'priority']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name} ({self.get_priority_display()})'
