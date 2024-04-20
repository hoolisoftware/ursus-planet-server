from django.contrib import admin

from . import models


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'datetime_start',
        'datetime_end'
    )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.SeasonParticipation)
class SeasonParticipationAdmin(admin.ModelAdmin):
    list_filter = (
        'season',
    )
    list_display = (
        'season',
        'user'
    )
