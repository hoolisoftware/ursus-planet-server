from django.contrib import admin

from . import models


class PlatformTaskLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'task',
        'reward',
        'got',
        'created'
    )


class PlatformTaskSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    fieldsets = (
        (
            "General settings",
            {
                "fields": ("cancel_fee", "referral_quote", "referral_comission"),
            },
        ),
    ) + tuple(
        (
            task[1],
            {
                "classes": ("collapse",),
                "fields": tuple(
                    f"{task[0]}_{setting[0]}"
                    for setting in models.TASK_SETTINGS
                ),
            },
        )
        for task in models.TASKS
    )
