from django.contrib.auth import get_user_model
from django.db import models
from core.models import SingletonModel

from apps.projects.models import Project

from .utils import (
    get_tasks_platform,
    get_tasks_platform_attrs
)


User = get_user_model()


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


class PlatformTaskLog(models.Model):
    CHOICES_TASK = (
        (task.name, task.title) for task in
        get_tasks_platform()
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    task = models.CharField(
        max_length=128,
        choices=CHOICES_TASK
    )

    got = models.BooleanField(default=False)
    reward = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'task'),)


class PlatformTaskSettings(SingletonModel):

    title = 'Platform Tasks settings'
    referral_quote = models.PositiveIntegerField(default=0)
    referral_interest = models.PositiveIntegerField(
        default=0,
        verbose_name='Referral interest (%)'
    )
    cancel_fee = models.PositiveIntegerField(
        default=0,
        verbose_name='Task cancel fee (%)'
    )

    class Meta:
        verbose_name_plural = 'Platform Tasks settings'

    @property
    def cancel_fee_factor(self):
        return self.cancel_fee / 100 + 1

    @property
    def referral_interest_factor(self):
        return self.referral_interest / 100


for task in get_tasks_platform():

    for attr in get_tasks_platform_attrs():

        PlatformTaskSettings.add_to_class(
            f'{task.name}_{attr[0]}',
            attr[1]()
        )


def ProjectField(related_name: str):
    return models.ForeignKey(
        ProjectProxy,
        on_delete=models.CASCADE,
        related_name=related_name,
        blank=False,
        null=True
    )
