from django.contrib import admin

from . import models


@admin.register(models.SocialAccountDiscord)
class SocialAccountDiscordAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'owner'
    )


@admin.register(models.SocialAccountX)
class SocialAccountXAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'owner'
    )


@admin.register(models.SocialAccountTelegram)
class SocialAccountTelegramAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'owner'
    )


@admin.register(models.SocialAccountTelegramCode)
class SocialAccountTelegramCodeAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'uuid',
        'datetime_created'
    )


@admin.register(models.SocialAccountGithub)
class SocialAccountGithubAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'owner'
    )