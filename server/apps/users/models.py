from django.db import models
from django.contrib.auth.models import AbstractUser

from image_optimizer.fields import OptimizedImageField

from .managers import UserManager


class User(AbstractUser):
    FREQUENCY_CHOICES = (
        ('fast', 'As fast as possible'),
        ('hour', 'Every hour'),
        ('day', 'Every day'),
        ('week', 'Every week'),
        ('month', 'Every month')
    )

    first_name = None
    last_name = None
    avatar = OptimizedImageField(
        upload_to='users/user/avatar/',
        optimized_image_output_size=(500, 500),
        optimized_image_resize_method="cover",
        null=True,
        blank=True
    )

    # notifications settings
    cabinet_notifications_email = models.BooleanField(default=False)
    cabinet_notifications_account = models.BooleanField(default=False)
    cabinet_notifications_frequency = models.CharField(choices=FREQUENCY_CHOICES, max_length=64, default='fast')
    project_notifications_email = models.BooleanField(default=False)
    project_notifications_account = models.BooleanField(default=False)
    project_notifications_frequency = models.CharField(choices=FREQUENCY_CHOICES, max_length=64, default='fast')

    objects = UserManager()
    
    def __str__(self):
        return self.username
