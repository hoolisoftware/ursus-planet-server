from django.db import models
from django.contrib.auth.models import AbstractUser

from image_optimizer.fields import OptimizedImageField

from .managers import UserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    avatar = OptimizedImageField(
        upload_to='users/user/avatar/',
        optimized_image_output_size=(500, 500),
        optimized_image_resize_method="cover",
        null=True,
        blank=True
    )

    objects = UserManager()
    
    def __str__(self):
        return self.username
