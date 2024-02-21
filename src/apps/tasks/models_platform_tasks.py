from django.contrib.auth import get_user_model
from django.db import models
from core.models import SingletonModel


User = get_user_model()


TASKS = (
    (
        'task_social_x',
        'Task - connect X account'
    ),
    (
        'task_social_github',
        'Task - connect GitHub account'
    ),
    (
        'task_social_discord',
        'Task - connect Discord account'
    ),
    (
        'task_social_telegram',
        'Task - connect Telegram account'
    ),
    (
        'task_email',
        'Task - set email'
    ),
    (
        'task_username',
        'Task - set username'
    ),
    (
        'task_domain_id',
        'Task - set domain id username'
    ),
    (
        'task_avatar',
        'Task - set avatar'
    ),
    (
        'task_avatar_nft',
        'Task - set avatar from NFT'
    ),
    (
        'task_avatar_nft_ursas',
        'Task - set avatar from NFT by Ursas collection'
    ),
    (
        'task_wallet',
        'Task - add wallet'
    ),
    (
        'task_chain',
        'Task - add chain'
    ),
    (
        'task_referral_self',
        'Task - set referral code'
    ),
    (
        'task_cabinet_notification_account',
        'Task - enable cabinet account notifications'
    ),
    (
        'task_cabinet_notification_email',
        'Task - enable cabinet email notifications'
    )
)


TASK_SETTINGS = (
    ('title', lambda: models.CharField(max_length=64)),
    ('link', lambda: models.CharField(max_length=64, blank=True, null=True)),
    ('reward', lambda: models.PositiveIntegerField(default=0)),
    ('is_active', lambda: models.BooleanField(default=False))
)


class PlatformTaskLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    got = models.BooleanField(default=False)
    reward = models.PositiveIntegerField(default=0)
    task = models.CharField(max_length=128, choices=TASKS)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'task'),)


class PlatformTaskSettings(SingletonModel):

    title = 'Platform Tasks settings'
    cancel_fee = models.PositiveIntegerField(default=0, verbose_name='Task cancel fee (%)')  # NOQA
    referral_quote = models.PositiveIntegerField(default=0)  # NOQA

    class Meta:
        verbose_name_plural = 'Platform Tasks settings'


for task in TASKS:
    for setting in TASK_SETTINGS:
        PlatformTaskSettings.add_to_class(
            f'{task[0]}_{setting[0]}',
            setting[1]()
        )
