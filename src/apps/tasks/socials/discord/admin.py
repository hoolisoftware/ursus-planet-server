from django.contrib import admin
from apps.tasks.admin import (
    LIST_DISPLAY_COMMON,
    TaskAdmin,
    admin_tasks
)

from . import models


class ServerSubscribeTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class ServerRoleTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class ServerBoostTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class ChannelMessageTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class ChannelMessageImageTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


class PostReactionTaskAdmin(TaskAdmin):
    list_display = LIST_DISPLAY_COMMON


admin_tasks.register(models.ServerSubscribeTask, ServerSubscribeTaskAdmin)
admin_tasks.register(models.ServerRoleTask, ServerRoleTaskAdmin)
admin_tasks.register(models.ServerBoostTask, ServerBoostTaskAdmin)
admin_tasks.register(models.ChannelMessageTask, ChannelMessageTaskAdmin)
admin_tasks.register(models.ChannelMessageImageTask, ChannelMessageImageTaskAdmin)
admin_tasks.register(models.PostReactionTask, PostReactionTaskAdmin)
