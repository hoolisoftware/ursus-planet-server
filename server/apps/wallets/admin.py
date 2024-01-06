from django.contrib import admin

from . import models


@admin.register(models.Chain)
class ChainAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        'chain_id',
        'name'
    )


@admin.register(models.UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        'user',
    )
    list_display = (
        'hash',
        'user'
    )


@admin.register(models.ProjectWallet)
class ProjectWalletAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        'project',
    )
    list_display = (
        'hash',
        'project'
    )