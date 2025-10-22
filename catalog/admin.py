from django.contrib import admin
from .models import Position, TaskType, Task, Worker

admin.site.register(Position)
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(Worker)
