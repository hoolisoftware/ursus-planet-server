from django.contrib.auth import get_user_model
from django.db import models
from abc import abstractmethod

from core.models import SingletonModel, ABCModel
from .api.exceptions import AlreadyGotRewardException


User = get_user_model()


class TaskSettings(SingletonModel):

    title = 'Task settings'
    referral_interest = models.PositiveIntegerField(
        default=0,
        verbose_name='Referral interest (%)'
    )
    cancel_fee = models.PositiveIntegerField(
        default=0,
        verbose_name='Task cancel fee (%)'
    )

    class Meta:
        verbose_name_plural = 'Tasks settings'

    @property
    def cancel_fee_factor(self):
        return self.cancel_fee / 100 + 1

    @property
    def referral_interest_factor(self):
        return self.referral_interest / 100


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
