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


class PlatformTasksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    fields = (
        (
            'task_social_reward',
            'task_social_is_active'
        ),
        (
            'task_email_reward',
            'task_email_is_active'
        ),
        (
            'task_username_reward',
            'task_username_is_active'
        ),
        (
            'task_domain_id_reward',
            'task_domain_id_is_active'
        ),
        (
            'task_avatar_reward',
            'task_avatar_is_active'
        ),
        (
            'task_nft_avatar_reward',
            'task_nft_avatar_is_active'
        ),
        (
            'task_ursas_collection_nft_avatar_reward',
            'task_ursas_collection_nft_avatar_is_active'
        ),
        (
            'task_wallet_reward',
            'task_wallet_is_active'
        ),
        (
            'task_chain_reward',
            'task_chain_is_active'
        ),
        (
            'task_referral_reward',
            'task_referral_is_active'
        ),
        (
            'task_email_notification_reward',
            'task_email_notification_is_active'
        ),
        (
            'task_cabinet_notification_reward',
            'task_cabinet_notification_is_active'
        ),
    )


admin_tasks = TaskAdminSite(name='admin_tasks')
admin_platform_tasks = TaskAdminSite(name='admin_platform_tasks')

admin_tasks.register(models.ProjectProxy, ProjectProxyAdmin)
admin_platform_tasks.register(models.PlatformTasks, PlatformTasksAdmin)
