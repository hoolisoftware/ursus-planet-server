from django.contrib import admin

from apps.tasks.admin import (
    LIST_DISPLAY_COMMON,
    TaskAdmin,
    admin_tasks
)

from . import models


class ChannelJoinTaskAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_COMMON

class GroupJoinTaskAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_COMMON

class GroupMessageTaskAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_COMMON

class ChannelReactionTaskAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_COMMON

class ChannelBoostTaskAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY_COMMON


admin_tasks.register(models.ChannelJoinTask, ChannelJoinTaskAdmin)
admin_tasks.register(models.GroupJoinTask, GroupJoinTaskAdmin)
admin_tasks.register(models.GroupMessageTask, GroupMessageTaskAdmin)
admin_tasks.register(models.ChannelReactionTask, ChannelReactionTaskAdmin)
admin_tasks.register(models.ChannelBoostTask, ChannelBoostTaskAdmin)