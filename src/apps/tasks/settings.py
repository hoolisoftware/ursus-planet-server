from django.db import models

from . import tasks_platform


INSTALLED_TASKS_PLATFORM = (
    tasks_platform.TaskUsername,
    tasks_platform.TaskEmail,
    tasks_platform.TaskAvatar,
    tasks_platform.TaskReferrer,
    tasks_platform.TaskCabinetNotificationsAccount,
    tasks_platform.TaskCabinetNotificationsEmail,
    tasks_platform.TaskSocialDiscord,
    tasks_platform.TaskSocialGithub,
    tasks_platform.TaskSocialTelegram,
    tasks_platform.TaskSocialX
)


INSTALLED_TASKS_PLATFORM_ATTRS = (
    (
        'title',
        lambda: models.CharField(max_length=64)
    ),
    (
        'link',
        lambda: models.CharField(
            max_length=64,
            blank=True,
            null=True
        )
    ),
    (
        'reward',
        lambda: models.PositiveIntegerField(default=0)
    ),
    (
        'is_active',
        lambda: models.BooleanField(default=False)
    )
)
