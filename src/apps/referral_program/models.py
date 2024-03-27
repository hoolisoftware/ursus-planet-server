from django.db import models

from core.models import SingletonModel


class ReferralProgramSettings(SingletonModel):
    title = 'Referral program settings'
    referral_genesis_user = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)  # NOQA
    referral_quote = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Referral program settings'
        verbose_name = 'Referral program settings'


class AbstractUserWithReferralProgram(models.Model):

    referrer = models.ForeignKey(
        "self",
        related_name='referrals',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    referral_quote = models.PositiveIntegerField(default=0)
    points_referrer = models.IntegerField(default=0)

    class Meta:
        abstract = True

    @property
    def referral_count(self):
        return self.referrals.count()
