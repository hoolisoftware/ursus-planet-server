from django.db import models

from apps.tasks.models import Task, ProjectField


class ProfileMixin(models.Model):
    link_profile = models.URLField()

    class Meta:
        abstract = True


class RepositoryMixin(models.Model):
    link_repository = models.URLField()

    class Meta:
        abstract = True


class ProfileFollowTask(ProfileMixin, Task):
    project = ProjectField('github_profile_follow')


class RepositoryStarTask(RepositoryMixin, Task):
    project = ProjectField('github_repository_star')


class RepositoryForkTask(RepositoryMixin, Task):
    project = ProjectField('github_repository_fork')
