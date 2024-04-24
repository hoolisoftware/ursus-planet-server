from django.apps import apps
from image_optimizer.fields import OptimizedImageField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

from apps.notifications.models import AbstractUserWithNotificationSettings
from apps.referral_program.models import AbstractUserWithReferralProgram
from apps.point_system.models import AbstractUserWithPointSystem

from .managers import UserManager
from .utils import random_hex
from .validators import (
    username_validator,
    username_forbidden_validator,
    avatar_validator
)


get_tasks_platform_settings = lambda: apps.get_model('tasks.TaskSettings').load()  # NOQA


class AbstractUserAvatarEmptyColors(models.Model):

    class Meta:
        abstract = True

    color1 = models.CharField(max_length=7, default=random_hex)
    color2 = models.CharField(max_length=7, default=random_hex)
    color3 = models.CharField(max_length=7, default=random_hex)
    color4 = models.CharField(max_length=7, default=random_hex)
    color5 = models.CharField(max_length=7, default=random_hex)


class User(
    AbstractUser,
    AbstractUserWithNotificationSettings,
    AbstractUserAvatarEmptyColors,
    AbstractUserWithReferralProgram,
    AbstractUserWithPointSystem
):

    objects = UserManager()

    USERNAME_FIELD = 'id'

    first_name = None
    last_name = None
    username = models.CharField(
        max_length=64,
        validators=[
            username_validator,
            username_forbidden_validator
        ],
        unique=True,
        blank=True,
        null=True
    )
    username_domain_id = models.CharField(
        max_length=64,
        validators=[
            username_validator,
            username_forbidden_validator
        ],
        unique=True,
        blank=True,
        null=True
    )
    username_as_domain_id = models.BooleanField(default=False)
    avatar = OptimizedImageField(
        upload_to='users/user/avatar/',
        optimized_image_output_size=(500, 500),
        optimized_image_resize_method="cover",
        null=True,
        blank=True,
        validators=[avatar_validator]
    )
    avatar_nft = OptimizedImageField(
        upload_to='users/user/avatar/',
        optimized_image_output_size=(500, 500),
        optimized_image_resize_method="cover",
        null=True,
        blank=True,
        validators=[avatar_validator]
    )
    avatar_as_nft = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'User ({self.id}) {self.username}'

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.username_as_domain_id and not self.username_domain_id:
            raise ValidationError('Domain id username cannot be empty')  # noqa
        if self.avatar_as_nft and not self.avatar_nft:
            raise ValidationError('Avatar NFT cannot be empty')  # noqa


class UserEmailCode(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=6)
