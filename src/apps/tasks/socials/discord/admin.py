from django.contrib import admin
from apps.tasks.admin import (
    LIST_DISPLAY_COMMON,
    TaskAdmin,
    TaskPlatformAdmin,
    admin_tasks,
    admin_platform_tasks
)

from . import models


class ServerSubscribeTaskAdmin(TaskAdmin):
    pass


class ServerRoleTaskAdmin(TaskAdmin):
    pass


class ServerBoostTaskAdmin(TaskAdmin):
    pass


class ChannelMessageTaskAdmin(TaskAdmin):
    pass


class ChannelMessageImageTaskAdmin(TaskAdmin):
    pass


class PostReactionTaskAdmin(TaskAdmin):
    pass


class ServerSubscribeTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class ServerRoleTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class ServerBoostTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class ChannelMessageTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class ChannelMessageImageTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class PostReactionTaskPlatformAdmin(TaskPlatformAdmin):
    pass



admin_tasks.register(models.ServerSubscribeTask, ServerSubscribeTaskAdmin)
admin_tasks.register(models.ServerRoleTask, ServerRoleTaskAdmin)
admin_tasks.register(models.ServerBoostTask, ServerBoostTaskAdmin)
admin_tasks.register(models.ChannelMessageTask, ChannelMessageTaskAdmin)
admin_tasks.register(models.ChannelMessageImageTask, ChannelMessageImageTaskAdmin)
admin_tasks.register(models.PostReactionTask, PostReactionTaskAdmin)

admin_platform_tasks.register(models.ServerSubscribeTask, ServerSubscribeTaskPlatformAdmin)
admin_platform_tasks.register(models.ServerRoleTask, ServerRoleTaskPlatformAdmin)
admin_platform_tasks.register(models.ServerBoostTask, ServerBoostTaskPlatformAdmin)
admin_platform_tasks.register(models.ChannelMessageTask, ChannelMessageTaskPlatformAdmin)
admin_platform_tasks.register(models.ChannelMessageImageTask, ChannelMessageImageTaskPlatformAdmin)
admin_platform_tasks.register(models.PostReactionTask, PostReactionTaskPlatformAdmin)