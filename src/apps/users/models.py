from django.db import models
from django.contrib.auth.models import AbstractUser

from image_optimizer.fields import OptimizedImageField

from .managers import UserManager
from .utils import random_hex
from .validators import username_validator


class User(AbstractUser):

    objects = UserManager()

    USERNAME_FIELD = 'id'

    FREQUENCY_CHOICES = (
        ('fast', 'As fast as possible'),
        ('hour', 'Every hour'),
        ('day', 'Every day'),
        ('week', 'Every week'),
        ('month', 'Every month')
    )

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
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    first_name = None
    last_name = None
    points = models.FloatField(default=0)

    # cabinet notifications settings
    cabinet_notifications_email = models.BooleanField(default=False)
    cabinet_notifications_account = models.BooleanField(default=False)
    cabinet_notifications_frequency = models.CharField(
        choices=FREQUENCY_CHOICES,
        max_length=64,
        default='fast'
    )
    # project notifications settings
    project_notifications_email = models.BooleanField(default=False)
    project_notifications_account = models.BooleanField(default=False)
    project_notifications_frequency = models.CharField(
        choices=FREQUENCY_CHOICES,
        max_length=64,
        default='fast'
    )

    # default avatar colors
    color1 = models.CharField(max_length=7, default=random_hex)
    color2 = models.CharField(max_length=7, default=random_hex)
    color3 = models.CharField(max_length=7, default=random_hex)
    color4 = models.CharField(max_length=7, default=random_hex)
    color5 = models.CharField(max_length=7, default=random_hex)

    def __str__(self):
        return f"{self.username}({self.id})"


class UserEmailCode(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=6)
