from django.contrib import admin
from django.contrib.admin import AdminSite

from apps.projects.admin import ProjectAdmin

from . import models
from . import utils


LIST_DISPLAY_COMMON = [
    'project',
    'created'
]

LIST_DISPLAY_PLATFORM = [
    'created',
]


class TaskAdminSite(AdminSite):
    site_header = "Tasks admin panel"
    site_title = "Tasks admin panel"


class PlatformTaskAdminSite(AdminSite):
    site_header = "Platform tasks admin panel"
    site_title = "Platform tasks admin panel"


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
                "fields": (
                    "cancel_fee",
                    "referral_genesis_user",
                    "referral_quote",
                    "referral_interest"
                ),
            },
        ),
    ) + tuple(
        (
            task.title,
            {
                "classes": ("collapse",),
                "fields": tuple(
                    f"{task.name}_{attr[0]}"
                    for attr in utils.get_tasks_platform_attrs()
                ),
            },
        )
        for task in utils.get_tasks_platform()
    )


class TaskAdmin(admin.ModelAdmin):
    autocomplete_fields = ('project',)
    list_display = LIST_DISPLAY_COMMON

    def get_queryset(self, request):
        return super(TaskAdmin, self).get_queryset(request).filter(project__isnull=False)  # NOQA


class TaskPlatformAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_PLATFORM
    exclude = ('project',)

    def get_queryset(self, request):
        return super(TaskPlatformAdmin, self).get_queryset(request).filter(project__isnull=True)  # NOQA


class ProjectProxyAdmin(ProjectAdmin):
    exclude = ('owner',)
    autocomplete_fields = []


admin_tasks = TaskAdminSite(name='admin_tasks')
admin_platform_tasks = TaskAdminSite(name='admin_platform_tasks')

admin_tasks.register(
    models.ProjectProxy,
    ProjectProxyAdmin
)
admin_platform_tasks.register(
    models.PlatformTaskSettings,
    PlatformTaskSettingsAdmin
)
admin_platform_tasks.register(
    models.PlatformTaskLog,
    PlatformTaskLogAdmin
)
