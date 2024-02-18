from django.contrib.auth import get_user_model
from django.db import models
from core.models import SingletonModel


User = get_user_model()


class PlatformTaskLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    got = models.BooleanField(default=False)
    reward = models.PositiveIntegerField()

    class Meta:
        abstract = True


class TaskSocialXLog(PlatformTaskLog):
    pass


class TaskSocialGithubLog(PlatformTaskLog):
    pass


class TaskSocialDiscordLog(PlatformTaskLog):
    pass


class TaskSocialTelegramLog(PlatformTaskLog):
    pass


class TaskEmailLog(PlatformTaskLog):
    pass


class TaskUsernameLog(PlatformTaskLog):
    pass


class TaskDomainIdLog(PlatformTaskLog):
    pass


class TaskAvatarLog(PlatformTaskLog):
    pass


class TaskNftAvatarLog(PlatformTaskLog):
    pass


class TaskUrsasCollectionNftAvatarLog(PlatformTaskLog):
    pass


class TaskWalletLog(PlatformTaskLog):
    pass


class TaskChainLog(PlatformTaskLog):
    pass


class TaskReferralSelfLog(PlatformTaskLog):
    pass


class TaskEmailNotificationLog(PlatformTaskLog):
    pass


class TaskCabinetNotificationLog(PlatformTaskLog):
    pass


class PlatformTasksSettings(SingletonModel):

    title = 'Platform Tasks settings'

    cancel_fee = models.PositiveIntegerField(default=0, verbose_name='Task cancel fee (%)')  # NOQA

    task_social_x_title = models.CharField(max_length=64)
    task_social_x_reward = models.PositiveIntegerField(default=0)
    task_social_x_is_active = models.BooleanField(default=False)
    task_social_x_link = models.CharField(max_length=64, blank=True, null=True)

    task_social_github_title = models.CharField(max_length=64)
    task_social_github_reward = models.PositiveIntegerField(default=0)
    task_social_github_is_active = models.BooleanField(default=False)
    task_social_github_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_social_discord_title = models.CharField(max_length=64)
    task_social_discord_reward = models.PositiveIntegerField(default=0)
    task_social_discord_is_active = models.BooleanField(default=False)
    task_social_discord_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_social_telegram_title = models.CharField(max_length=64)
    task_social_telegram_reward = models.PositiveIntegerField(default=0)
    task_social_telegram_is_active = models.BooleanField(default=False)
    task_social_telegram_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_email_title = models.CharField(max_length=64)
    task_email_reward = models.PositiveIntegerField(default=0)
    task_email_is_active = models.BooleanField(default=False)
    task_email_link = models.CharField(max_length=64, blank=True, null=True)

    task_username_title = models.CharField(max_length=64)
    task_username_reward = models.PositiveIntegerField(default=0)
    task_username_is_active = models.BooleanField(default=False)
    task_username_link = models.CharField(max_length=64, blank=True, null=True)

    task_domain_id_title = models.CharField(max_length=64)
    task_domain_id_reward = models.PositiveIntegerField(default=0)
    task_domain_id_is_active = models.BooleanField(default=False)
    task_domain_id_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_avatar_title = models.CharField(max_length=64)
    task_avatar_reward = models.PositiveIntegerField(default=0)
    task_avatar_is_active = models.BooleanField(default=False)
    task_avatar_link = models.CharField(max_length=64, blank=True, null=True)

    task_nft_avatar_title = models.CharField(max_length=64)
    task_nft_avatar_reward = models.PositiveIntegerField(default=0)
    task_nft_avatar_is_active = models.BooleanField(default=False)
    task_nft_avatar_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_ursas_collection_nft_avatar_title = models.CharField(max_length=64)
    task_ursas_collection_nft_avatar_reward = models.PositiveIntegerField(default=0)  # NOQA
    task_ursas_collection_nft_avatar_is_active = models.BooleanField(default=False)  # NOQA
    task_ursas_collection_nft_avatar_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_wallet_title = models.CharField(max_length=64)
    task_wallet_reward = models.PositiveIntegerField(default=0)
    task_wallet_is_active = models.BooleanField(default=False)
    task_wallet_link = models.CharField(max_length=64, blank=True, null=True)

    task_chain_title = models.CharField(max_length=64)
    task_chain_reward = models.PositiveIntegerField(default=0)
    task_chain_is_active = models.BooleanField(default=False)
    task_chain_link = models.CharField(max_length=64, blank=True, null=True)

    task_referral_self_title = models.CharField(max_length=64)
    task_referral_self_reward = models.PositiveIntegerField(default=0)
    task_referral_self_is_active = models.BooleanField(default=False)
    task_referral_self_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_email_notification_title = models.CharField(max_length=64)
    task_email_notification_reward = models.PositiveIntegerField(default=0)
    task_email_notification_is_active = models.BooleanField(default=False)
    task_email_notification_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    task_cabinet_notification_title = models.CharField(max_length=64)
    task_cabinet_notification_reward = models.PositiveIntegerField(default=0)
    task_cabinet_notification_is_active = models.BooleanField(default=False)
    task_cabinet_notification_link = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    class Meta:
        verbose_name_plural = 'Platform Tasks settings'
