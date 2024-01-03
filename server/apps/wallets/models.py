from django.contrib.auth import get_user_model
from django.db import models

from apps.projects.models import Project


User = get_user_model()


class ProjectWallet(models.Model):
    hash = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.hash} (project wallet)'


class UserWallet(models.Model):
    hash = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.hash} (user wallet)'