from django.db import models
from core.models import SingletonModel

from apps.tasks.models import TaskLog
from .utils import (
    get_tasks_platform,
    get_tasks_platform_attrs
)


class PlatformTaskLog(TaskLog):
    CHOICES_TASK = (
        (task.name, task.title) for task in
        get_tasks_platform()
    )
    task = models.CharField(max_length=128, choices=CHOICES_TASK)


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
