from django.db import models

from . import tasks


INSTALLED_TASKS_PLATFORM = (
    tasks.TaskUsername,
    tasks.TaskEmail,
    tasks.TaskAvatar,
    tasks.TaskReferrer,
    tasks.TaskCabinetNotificationsAccount,
    tasks.TaskCabinetNotificationsEmail,
    tasks.TaskSocialDiscord,
    tasks.TaskSocialGithub,
    tasks.TaskSocialTelegram,
    tasks.TaskSocialX
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
