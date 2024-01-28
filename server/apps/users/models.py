from django.core.validators import RegexValidator
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

    # TODO: add username validation
    username = models.CharField(
        max_length=64,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z][\w.@+-]{4,15}+\Z',
                message = (
                    "Enter a valid username. This value may contain only letters, "
                    "numbers, and @/./+/-/_ characters, start from letter, and have length between 4 and 16 characters."
                )
            )
        ],
        blank=True,
        null=True
    )
    email = models.EmailField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
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
    
    USERNAME_FIELD = 'id'

    def __str__(self):
        return f"{self.username}({self.id})"


class UserEmailCode(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=6)
