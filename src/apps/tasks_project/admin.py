from django.contrib import admin


from . import models


@admin.register(models.TaskCustom)
class TaskCustomAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link',
        'reward',
        'created',
        'expiration',
        'description'
    )


@admin.register(models.TaskCustomLog)
class TaskCustomLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'task',
        'reward',
        'created'
    )
