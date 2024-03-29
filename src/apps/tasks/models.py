from django.contrib.auth import get_user_model
from django.db import models
from abc import abstractmethod

from core.models import ABCModel
from .api.exceptions import AlreadyGotRewardException


class TaskLog(ABCModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    got = models.BooleanField(default=False)
    reward = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        # unique_together = (('user', 'task'),)

    @property
    @abstractmethod
    def task(self):
        pass

    def withdraw_points(self):
        if self.got:
            raise AlreadyGotRewardException

        self.user.add_points(points=self.reward)
        self.got = True
        self.save()
