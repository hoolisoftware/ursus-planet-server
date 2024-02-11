from django.contrib import admin
from django.contrib.admin import AdminSite

from apps.projects.admin import ProjectAdmin

from . import models


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

admin_tasks.register(models.ProjectProxy, ProjectProxyAdmin)
