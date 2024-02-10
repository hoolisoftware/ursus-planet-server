from django.contrib import admin

from apps.tasks.admin import (
    LIST_DISPLAY_COMMON,
    TaskAdmin,
    admin_tasks
)

from . import models


class ProfileFollowTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class RepositoryStarTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class RepositoryForkTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


admin_tasks.register(models.ProfileFollowTask, ProfileFollowTaskAdmin)
admin_tasks.register(models.RepositoryStarTask, RepositoryStarTaskAdmin)
admin_tasks.register(models.RepositoryForkTask, RepositoryForkTaskAdmin)