from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.referral_program.models import ReferralProgramSettings
from ..models import PlatformTaskLog, PlatformTasks
from ..utils import get_tasks_platform

User = get_user_model()


@receiver(pre_save, sender=User)
def user_handler(sender, instance, **kwargs):
    tasks = PlatformTasks.load()
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
                    reward=getattr(tasks, f'{task.name}_reward')
                )
        elif log:
            if log.got and (task in cancellable_tasks):
                instance.cancel_points(log.reward)
                log.delete()


@receiver(post_save, sender=User)
def user_create_handler(sender, instance, created, **kwargs):

    instance.referral_quote = ReferralProgramSettings.load().referral_quote
