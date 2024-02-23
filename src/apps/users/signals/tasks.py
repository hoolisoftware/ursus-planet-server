from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.tasks.models import PlatformTaskLog, PlatformTaskSettings
from apps.tasks.utils import get_tasks_platform

User = get_user_model()


@receiver(pre_save, sender=User)
def user_handler(sender, instance, **kwargs):
    settings = PlatformTaskSettings.load()
    logs = PlatformTaskLog.objects.filter(user=instance)

    cancellable_tasks = filter(
        lambda task: (
            task.app == 'users' and
            task.cancellable
        ),
        get_tasks_platform()
    )

    for task in get_tasks_platform():

        log = logs.filter(task=task.name).first()

        if getattr(instance, task.name.replace('task_', ''), None):
            if not log:
                PlatformTaskLog.objects.create(
                    task=task.name,
                    user=instance,
                    reward=getattr(settings, f'{task.name}_reward')
                )
        elif log:
            if log.got and (task in cancellable_tasks):
                instance.cancel_points(log.reward)
                log.delete()


@receiver(post_save, sender=User)
def user_create_handler(sender, instance, created, **kwargs):
    settings = PlatformTaskSettings.load()

    instance.referral_quote = settings.referral_quote
