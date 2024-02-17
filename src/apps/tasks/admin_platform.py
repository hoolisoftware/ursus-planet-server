from django.contrib import admin


class TaskUsernameLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'reward',
        'got'
    )
