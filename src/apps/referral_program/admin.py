from django.contrib import admin

from . import models


@admin.register(models.ReferralProgramSettings)
class ReferralProgramSettingsAdmin(admin.ModelAdmin):
    list_display = ('title', )
