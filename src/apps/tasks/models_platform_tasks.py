from django.contrib.auth import get_user_model
from django.db import models
from core.models import SingletonModel


User = get_user_model()


class PlatformTaskLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    got = models.BooleanField()
    reward = models.PositiveIntegerField()

    class Meta:
        abstract = True


class TaskUsernameLog(PlatformTaskLog):
    pass


class PlatformTasksSettings(SingletonModel):

    title = 'Platform Tasks settings'

    cancel_fee = models.PositiveIntegerField(default=0, verbose_name='Task cancel fee (%)')  # NOQA

    task_social_reward = models.PositiveIntegerField(default=0)
    task_social_is_active = models.BooleanField()

    task_email_reward = models.PositiveIntegerField(default=0)
    task_email_is_active = models.BooleanField()

    task_username_reward = models.PositiveIntegerField(default=0)
    task_username_is_active = models.BooleanField()
    task_username_link = models.URLField(blank=True, null=True)

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

    class Meta:
        verbose_name_plural = 'Platform Tasks settings'
