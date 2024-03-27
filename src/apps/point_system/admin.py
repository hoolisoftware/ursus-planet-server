from django.contrib import admin

from . import models


@admin.register(models.PointSystemSettings)
class PointSystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('title', )
