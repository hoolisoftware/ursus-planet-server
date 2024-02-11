from apps.tasks.admin import (
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
admin_tasks.register(models.ChannelMessageImageTask, ChannelMessageImageTaskAdmin)  # NOQA
admin_tasks.register(models.PostReactionTask, PostReactionTaskAdmin)

admin_platform_tasks.register(models.ServerSubscribeTask, ServerSubscribeTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.ServerRoleTask, ServerRoleTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.ServerBoostTask, ServerBoostTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.ChannelMessageTask, ChannelMessageTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.ChannelMessageImageTask, ChannelMessageImageTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.PostReactionTask, PostReactionTaskPlatformAdmin)  # NOQA
