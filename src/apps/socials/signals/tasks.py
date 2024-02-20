from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from apps.tasks.models import PlatformTaskLog, PlatformTaskSettings
from .. import models


def create_social_create_handler(social, social_task_name):
    @receiver(pre_save, sender=social)
    def handler(sender, instance, **kwargs):
        log = PlatformTaskLog.objects.filter(
            user=instance.owner,
            task=social_task_name
        ).first()
        settings = PlatformTaskSettings.load()

        if not log:
            PlatformTaskLog.objects.create(
                task=social_task_name,
                user=instance.owner,
                reward=settings.task_username_reward
            )

    return handler


def create_social_delete_handler(social, social_task_name):
    @receiver(pre_delete, sender=social)
    def handler(sender, instance, **kwargs):
        log = PlatformTaskLog.objects.filter(
            user=instance.owner,
            task=social_task_name
        ).first()

        if log and log.got:
            log.user.points -= log.reward
            log.delete()
            log.user.save()

    return handler


handler_create_discord = create_social_create_handler(models.SocialAccountDiscord, 'task_social_discord')  # NOQA
handler_create_telegram = create_social_create_handler(models.SocialAccountTelegram, 'task_social_telegram')  # NOQA
handler_create_github = create_social_create_handler(models.SocialAccountGithub, 'task_social_github')  # NOQA
handler_create_x = create_social_create_handler(models.SocialAccountX, 'task_social_x')  # NOQA

handler_delete_discord = create_social_delete_handler(models.SocialAccountDiscord, 'task_social_discord')  # NOQA
handler_delete_telegram = create_social_delete_handler(models.SocialAccountTelegram, 'task_social_telegram')  # NOQA
handler_delete_github = create_social_delete_handler(models.SocialAccountGithub, 'task_social_github')  # NOQA
handler_delete_x = create_social_delete_handler(models.SocialAccountX, 'task_social_x')  # NOQA
