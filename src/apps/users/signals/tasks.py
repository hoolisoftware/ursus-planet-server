from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.tasks.models import PlatformTaskLog, PlatformTaskSettings


User = get_user_model()


@receiver(pre_save, sender=User)
def user_handler(sender, instance, **kwargs):
    settings = PlatformTaskSettings.load()
    logs = PlatformTaskLog.objects.filter(user=instance)

    if instance.username:
        if not logs.filter(task='task_username').first():
            PlatformTaskLog.objects.create(
                task='task_username',
                user=instance,
                reward=settings.task_username_reward
            )

    if instance.avatar:
        if not logs.filter(task='task_avatar').first():
            PlatformTaskLog.objects.create(
                task='task_avatar',
                user=instance,
                reward=settings.task_avatar_reward
            )
    if instance.email:
        if not logs.filter(task='task_email').first():
            PlatformTaskLog.objects.create(
                task='task_email',
                user=instance,
                reward=settings.task_email_reward
            )

    if instance.referrer:
        if not logs.filter(task='task_referral_self').first():
            PlatformTaskLog.objects.create(
                task='task_referral_self',
                user=instance,
                reward=settings.task_referral_self_reward
            )

    enabled = instance.cabinet_notifications_account
    log = logs.filter(task='task_cabinet_notification_account').first()
    if enabled and (not log):
        PlatformTaskLog.objects.create(
            task='task_cabinet_notification_account',
            user=instance,
            reward=settings.task_cabinet_notification_account_reward
        )
    elif (not enabled) and log:
        if log.got:
            instance.points = instance.points - (log.reward * (settings.cancel_fee / 100 + 1))  # NOQA
            instance.referrer.points_referral -= round(log.reward * (settings.cancel_fee + 1) * settings.referral_comission / 100 / 100, 1)  # NOQA
            instance.referrer.save()
        log.delete()
        instance.save()

    enabled = instance.cabinet_notifications_email
    log = logs.filter(task='task_cabinet_notification_email').first()
    if enabled and (not log):
        PlatformTaskLog.objects.create(
            task='task_cabinet_notification_email',
            user=instance,
            reward=settings.task_cabinet_notification_email_reward
        )
    elif (not enabled) and log:
        if log.got:
            instance.points = instance.points - (log.reward * (settings.cancel_fee / 100 + 1))  # NOQA
            instance.referrer.points_referral -= round(log.reward * (settings.cancel_fee + 100) * settings.referral_comission / 100 / 100, 1)  # NOQA
            instance.referrer.save()
        log.delete()
        instance.save()
