from django.db import models

from core.models import SingletonModel


class PointSystemSettings(SingletonModel):
    title = 'Point system settings'
    cancel_fee = models.PositiveIntegerField(verbose_name='Cancel fee (%)', default=0)  # noqa
    referrer_interest = models.PositiveIntegerField(verbose_name='Referrer interest (%)', default=0)  # noqa

    class Meta:
        verbose_name = 'Point system settings'
        verbose_name_plural = 'Point system settings'

    @property
    def cancel_fee_factor(self):
        return self.cancel_fee / 100 + 1

    @property
    def referrer_interest_factor(self):
        return self.referrer_interest / 100


class AbstractUserWithPointSystem(models.Model):
    points = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def add_points(
        self,
        points: int,
        with_referrer_interest: bool = True,
        to_referral_program: bool = False
    ) -> None:
        if to_referral_program:
            self.points_referrer += points
        else:
            self.points += points
        self.save()

        if with_referrer_interest and self.referrer:
            self.referrer.add_points(
                points * PointSystemSettings.load().referrer_interest_factor,
                with_referrer_interest=False,
                to_referral_program=True
            )

    def cancel_points(
        self,
        points: int,
        with_referrer_interest: bool = True
    ) -> None:
        self.add_points(
            points=(-points * PointSystemSettings.load().cancel_fee_factor),
            with_referrer_interest=with_referrer_interest
        )
