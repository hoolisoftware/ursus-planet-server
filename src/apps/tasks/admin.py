from django.contrib import admin
from django.contrib.admin import AdminSite

from apps.projects.admin import ProjectAdmin

from . import models
from . import admin_platform


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


class PlatformTasksSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    fieldsets = (
        (
            "General settings",
            {
                "fields": ("cancel_fee",),
            },
        ),
        (
            "Task - connect X account",
            {
                "fields": (
                    (
                        'task_social_x_reward',
                        'task_social_x_is_active'
                    ),
                    'task_social_x_title',
                    'task_social_x_link'
                ),
            },
        ),
        (
            'Task - connect Github account',
            {
                "fields": (
                    (
                        'task_social_github_reward',
                        'task_social_github_is_active'
                    ),
                    'task_social_github_title',
                    'task_social_github_link'
                ),
            }
        ),
        (
            'Task - connect discord account',
            {
                "fields": (
                    (
                        'task_social_discord_reward',
                        'task_social_discord_is_active',
                    ),
                    'task_social_discord_title',
                    'task_social_discord_link'
                ),
            }
        ),
        (
            'Task - connect telegram account',
            {
                "fields": (
                    (
                        'task_social_telegram_reward',
                        'task_social_telegram_is_active',  
                    ),
                    'task_social_telegram_title',
                    'task_social_telegram_link'
                ),
            }
        ),
        (
            'Task - connect email',
            {
                "fields": (
                    (
                        'task_email_reward',
                        'task_email_is_active'
                    ),
                    'task_email_title',
                    'task_email_link'
                ),
            }
        ),
        (
            'Task - set username',
            {
                "fields": (
                    (
                        'task_username_reward',
                        'task_username_is_active'
                    ),
                    'task_username_title',
                    'task_username_link'
                ),
            }
        ),
        (
            'Task - set domain as username',
            {
                "fields": (
                    (
                        'task_domain_id_reward',
                        'task_domain_id_is_active'
                    ),
                    'task_domain_id_title',
                    'task_domain_id_link'
                ),
            }
        ),
        (
            'Task - set avatar',
            {
                "fields": (
                    (
                        'task_avatar_reward',
                        'task_avatar_is_active'
                    ),
                    'task_avatar_title',
                    'task_avatar_link'
                ),
            }
        ),
        (
            'Task - set NFT as an avatar',
            {
                "fields": (
                    (
                        'task_nft_avatar_reward',
                        'task_nft_avatar_is_active'
                    ),
                    'task_nft_avatar_title',
                    'task_nft_avatar_link'
                ),
            }
        ),
        (
            'Task - set NFT from ursas collection as an avatar',
            {
                "fields": (
                    (
                        'task_ursas_collection_nft_avatar_reward',
                        'task_ursas_collection_nft_avatar_is_active'
                    ),
                    'task_ursas_collection_nft_avatar_title',
                    'task_ursas_collection_nft_avatar_link'
                ),
            }
        ),
        (
            'Task - connect wallet',
            {
                "fields": (
                    (
                        'task_wallet_reward',
                        'task_wallet_is_active'
                    ),
                    'task_wallet_title',
                    'task_wallet_link'
                ),
            }
        ),
        (
            'Task - add chain',
            {
                "fields": (
                    (
                        'task_chain_reward',
                        'task_chain_is_active'
                    ),
                    'task_chain_title',
                    'task_chain_link'
                ),
            }
        ),
        (
            'Task - become a referral',
            {
                "fields": (
                    (
                        'task_referral_self_reward',
                        'task_referral_self_is_active'
                    ),
                    'task_referral_self_title',
                    'task_referral_self_link'
                ),
            }
        ),
        (
            'Task - enable email notification',
            {
                "fields": (
                    (
                        'task_email_notification_reward',
                        'task_email_notification_is_active'
                    ),
                    'task_email_notification_title',
                    'task_email_notification_link'
                ),
            }
        ),
        (
            'Task - enable cabitnet notification',
            {
                "fields": (
                    (
                        'task_cabinet_notification_reward',
                        'task_cabinet_notification_is_active'
                    ),
                    'task_cabinet_notification_title',
                    'task_cabinet_notification_link'
                ),
            }
        ),
    )


admin_tasks = TaskAdminSite(name='admin_tasks')
admin_platform_tasks = TaskAdminSite(name='admin_platform_tasks')

admin_tasks.register(models.ProjectProxy, ProjectProxyAdmin)
admin_platform_tasks.register(models.PlatformTasksSettings, PlatformTasksSettingsAdmin)  # NOQA

admin_platform_tasks.register(models.TaskUsernameLog, admin_platform.TaskUsernameLogAdmin)  # NOQA
