from django.db import models

from apps.users.models import User
from apps.projects.models import Project


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    reward = models.PositiveIntegerField()

    class Meta:
        abstract = True


class ProjectProxy(Project):
    class Meta:
        proxy = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        

def ProjectField(related_name: str):
    return models.ForeignKey(
        ProjectProxy,
        on_delete=models.CASCADE,
        related_name=related_name,
        blank=False, 
        null=True
    )
