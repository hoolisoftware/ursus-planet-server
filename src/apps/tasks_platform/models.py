from django.contrib.auth import get_user_model
from django.db import models
from core.models import SingletonModel


from .utils import (
    get_tasks_platform,
    get_tasks_platform_attrs
)


User = get_user_model()


class PlatformTaskLog(models.Model):
    CHOICES_TASK = (
        (task.name, task.title) for task in
        get_tasks_platform()
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.CharField(max_length=128, choices=CHOICES_TASK)

    got = models.BooleanField(default=False)
    reward = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'task'),)


class PlatformTasks(SingletonModel):

    title = 'Tasks'

    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'


for task in get_tasks_platform():

    for attr in get_tasks_platform_attrs():

        PlatformTasks.add_to_class(
            f'{task.name}_{attr[0]}',
            attr[1]()
        )
