from decimal import Decimal

from django.apps import apps
from image_optimizer.fields import OptimizedImageField
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from .utils import random_hex
from .validators import username_validator


get_tasks_platform_settings = lambda: apps.get_model('tasks.PlatformTaskSettings').load()  # NOQA


class UserNotificationSettings(models.Model):

    class Meta:
        abstract = True

    FREQUENCY_CHOICES = (
        ('fast', 'As fast as possible'),
        ('hour', 'Every hour'),
        ('day', 'Every day'),
        ('week', 'Every week'),
        ('month', 'Every month')
    )

    cabinet_notifications_email = models.BooleanField(default=False)
    cabinet_notifications_account = models.BooleanField(default=False)
    cabinet_notifications_frequency = models.CharField(
        choices=FREQUENCY_CHOICES,
        max_length=64,
        default='fast'
    )

    project_notifications_email = models.BooleanField(default=False)
    project_notifications_account = models.BooleanField(default=False)
    project_notifications_frequency = models.CharField(
        choices=FREQUENCY_CHOICES,
        max_length=64,
        default='fast'
    )


class UserAvatarEmptyColors(models.Model):

    class Meta:
        abstract = True

    color1 = models.CharField(max_length=7, default=random_hex)
    color2 = models.CharField(max_length=7, default=random_hex)
    color3 = models.CharField(max_length=7, default=random_hex)
    color4 = models.CharField(max_length=7, default=random_hex)
    color5 = models.CharField(max_length=7, default=random_hex)


class UserReferral(models.Model):

    referrer = models.ForeignKey(
        "self",
        related_name='referrals',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    referral_quote = models.PositiveIntegerField(default=0)
    points_referral = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=1
    )

    class Meta:
        abstract = True

    @property
    def referral_count(self):
        return self.referrals.count()


class User(
    AbstractUser,
    UserNotificationSettings,
    UserAvatarEmptyColors,
    UserReferral,
):

    objects = UserManager()

    USERNAME_FIELD = 'id'

    first_name = None
    last_name = None
    username = models.CharField(
        max_length=64,
        validators=[username_validator],
        blank=True,
        null=True
    )
    avatar = OptimizedImageField(
        upload_to='users/user/avatar/',
        optimized_image_output_size=(500, 500),
        optimized_image_resize_method="cover",
        null=True,
        blank=True
    )
    points = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=1
    )
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    def add_points(
        self,
        points: int,
        referral_interest: bool = True,
        referral: bool = False
    ) -> None:
        points = round(points, 1)
        if referral:
            self.points_referral += Decimal(points)
        else:
            self.points += Decimal(points)
        self.save()

        if referral_interest and self.referrer:
            task_settings = get_tasks_platform_settings()

            self.referrer.add_points(
                points * task_settings.referral_interest_factor,
                referral_interest=False,
                referral=True
            )

    def cancel_points(
        self,
        points: int,
        referral_interest: bool = True
    ) -> None:
        task_settings = get_tasks_platform_settings()
        self.add_points(-points * task_settings.cancel_fee_factor)

    def __str__(self):
        return f"{self.username}({self.id})"


class UserEmailCode(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=6)
