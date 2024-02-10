from django.db import models

from apps.tasks.models import Task, ProjectField


class ChannelMixin(models.Model):
    link_channel = models.URLField()

    class Meta:
        abstract = True


class GroupMixin(models.Model):
    link_group = models.URLField()

    class Meta:
        abstract = True


class ChannelJoinTask(ChannelMixin, Task):
    project = ProjectField('telegram_channel_join')


class GroupJoinTask(GroupMixin, Task):
    project = ProjectField('telegram_group_join')


class GroupMessageTask(GroupMixin, Task):
    project = ProjectField('telegram_group_message')


class ChannelReactionTask(ChannelMixin, Task):
    project = ProjectField('telegram_channel_reaction')


class ChannelBoostTask(ChannelMixin, Task):
    project = ProjectField('telegram_channel_boost')
