from django.db import models

from apps.tasks.models import Task, ProjectField


class ServerMixin(models.Model):
    link_server = models.URLField()

    class Meta:
        abstract = True


class ChannelMixin(models.Model):
    link_channel = models.URLField()

    class Meta:
        abstract = True


class PostMixin(models.Model):
    link_post = models.URLField()

    class Meta:
        abstract = True


class ServerSubscribeTask(ServerMixin, Task):
    project = ProjectField('discord_server_subscribe')


class ServerRoleTask(ServerMixin, Task):
    project = ProjectField('discord_server_role')
    role = models.CharField(max_length=64)


class ServerBoostTask(ServerMixin, Task):
    project = ProjectField('discord_server_boost')


class ChannelMessageTask(ChannelMixin, Task):
    project = ProjectField('discord_channel_message')


class ChannelMessageImageTask(ChannelMixin, Task):
    project = ProjectField('discord_channel_message_image')


class PostReactionTask(PostMixin, Task):
    project = ProjectField('discord_channel_reaction')
    rn_postfix = 'channel_message'
