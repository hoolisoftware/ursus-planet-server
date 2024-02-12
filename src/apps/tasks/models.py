from django.db import models

from core.models import SingletonModel
from apps.projects.models import Project


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    reward = models.PositiveIntegerField()

    class Meta:
        abstract = True


class ProjectProxy(Project):
    class Meta:
        proxy = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class PlatformTasks(SingletonModel):

    title = 'Platform Tasks'

    task_social_reward = models.PositiveIntegerField(default=0)
    task_social_is_active = models.BooleanField()

    task_email_reward = models.PositiveIntegerField(default=0)
    task_email_is_active = models.BooleanField()

    task_username_reward = models.PositiveIntegerField(default=0)
    task_username_is_active = models.BooleanField()

    task_domain_id_reward = models.PositiveIntegerField(default=0)
    task_domain_id_is_active = models.BooleanField()

    task_avatar_reward = models.PositiveIntegerField(default=0)
    task_avatar_is_active = models.BooleanField()

    task_nft_avatar_reward = models.PositiveIntegerField(default=0)
    task_nft_avatar_is_active = models.BooleanField()

    task_ursas_collection_nft_avatar_reward = models.PositiveIntegerField(default=0)  # NOQA
    task_ursas_collection_nft_avatar_is_active = models.BooleanField()

    task_wallet_reward = models.PositiveIntegerField(default=0)
    task_wallet_is_active = models.BooleanField()

    task_chain_reward = models.PositiveIntegerField(default=0)
    task_chain_is_active = models.BooleanField()

    task_referral_reward = models.PositiveIntegerField(default=0)
    task_referral_is_active = models.BooleanField()

    task_email_notification_reward = models.PositiveIntegerField(default=0)
    task_email_notification_is_active = models.BooleanField()

    task_cabinet_notification_reward = models.PositiveIntegerField(default=0)
    task_cabinet_notification_is_active = models.BooleanField()


def ProjectField(related_name: str):
    return models.ForeignKey(
        ProjectProxy,
        on_delete=models.CASCADE,
        related_name=related_name,
        blank=False,
        null=True
    )
