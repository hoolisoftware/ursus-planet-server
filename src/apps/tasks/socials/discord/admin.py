from django.contrib import admin
from apps.tasks.admin import admin_tasks

from .models import Task

admin_tasks.register(Task)

