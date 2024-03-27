from django.contrib import admin

from . import models
from . import utils


LIST_DISPLAY_COMMON = [
    'project',
    'created'
]

LIST_DISPLAY_PLATFORM = [
    'created',
]


@admin.register(models.PlatformTaskLog)
class PlatformTaskLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'task',
        'reward',
        'got',
        'created'
    )


@admin.register(models.PlatformTasks)
class PlatformTasksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    fieldsets = tuple(
        (
            task.title,
            {
                "classes": ("collapse",),
                "fields": tuple(
                    f"{task.name}_{attr[0]}"
                    for attr in utils.get_tasks_platform_attrs()
                ),
            },
        )
        for task in utils.get_tasks_platform()
    )
