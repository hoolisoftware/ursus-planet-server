from django.contrib.auth import get_user_model
from django.db import models

from apps.projects.models import Project


User = get_user_model()


class Chain(models.Model):
    chain_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64, blank=True, null=True)  # NOQA

    def __str__(self):
        return f'{self.name}({self.chain_id})'


class Wallet(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.SET_NULL, null=True)  # NOQA
    hash = models.TextField()

    class Meta:
        abstract = True


class ProjectWallet(Wallet):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)  # NOQA

    def __str__(self):
        return f'{self.hash} (project wallet)'


class UserWallet(Wallet):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='wallets', null=True)  # NOQA

    def __str__(self):
        return f'{self.hash} (user wallet)'
