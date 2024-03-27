from django.db import models

from core.models import SingletonModel


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
