from apps.tasks.admin import (
    TaskAdmin,
    TaskPlatformAdmin,
    admin_tasks,
    admin_platform_tasks
)

from . import models


class ChannelJoinTaskAdmin(TaskAdmin):
    pass


class GroupJoinTaskAdmin(TaskAdmin):
    pass


class GroupMessageTaskAdmin(TaskAdmin):
    pass


class ChannelReactionTaskAdmin(TaskAdmin):
    pass


class ChannelBoostTaskAdmin(TaskAdmin):
    pass


class ChannelJoinTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class GroupJoinTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class GroupMessageTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class ChannelReactionTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class ChannelBoostTaskPlatformAdmin(TaskPlatformAdmin):
    pass


admin_tasks.register(models.ChannelJoinTask, ChannelJoinTaskAdmin)
admin_tasks.register(models.GroupJoinTask, GroupJoinTaskAdmin)
admin_tasks.register(models.GroupMessageTask, GroupMessageTaskAdmin)
admin_tasks.register(models.ChannelReactionTask, ChannelReactionTaskAdmin)
admin_tasks.register(models.ChannelBoostTask, ChannelBoostTaskAdmin)

admin_platform_tasks.register(models.ChannelJoinTask, ChannelJoinTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.GroupJoinTask, GroupJoinTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.GroupMessageTask, GroupMessageTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.ChannelReactionTask, ChannelReactionTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.ChannelBoostTask, ChannelBoostTaskPlatformAdmin)  # NOQA
