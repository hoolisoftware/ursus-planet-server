from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class TaskCustom(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    reward = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    expiration = models.DateTimeField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)


class TaskCustomLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskCustom, on_delete=models.CASCADE)
    reward = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'task'),)
