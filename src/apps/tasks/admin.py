from django.contrib import admin

from . import models


@admin.register(models.TaskSettings)
class TaskSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    fields = (
        "cancel_fee",
        "referral_interest"
    )
