from apps.tasks.admin import (
    TaskAdmin,
    TaskPlatformAdmin,
    admin_tasks,
    admin_platform_tasks
)

from . import models


class ProfileFollowTaskAdmin(TaskAdmin):
    pass


class TweetRepostTaskAdmin(TaskAdmin):
    pass


class TweetLikeTaskAdmin(TaskAdmin):
    pass


class TweetCommentExactTaskAdmin(TaskAdmin):
    pass


class TweetCommentTaskAdmin(TaskAdmin):
    pass


class TweetWatchVideoTaskAdmin(TaskAdmin):
    pass


class TweetTaskAdmin(TaskAdmin):
    pass


class ProfileFollowTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class TweetRepostTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class TweetLikeTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class TweetCommentExactTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class TweetCommentTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class TweetWatchVideoTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class TweetTaskPlatformAdmin(TaskPlatformAdmin):
    pass


admin_tasks.register(models.ProfileFollowTask, ProfileFollowTaskAdmin)
admin_tasks.register(models.TweetRepostTask, TweetRepostTaskAdmin)
admin_tasks.register(models.TweetLikeTask, TweetLikeTaskAdmin)
admin_tasks.register(models.TweetCommentExactTask, TweetCommentExactTaskAdmin)
admin_tasks.register(models.TweetCommentTask, TweetCommentTaskAdmin)
admin_tasks.register(models.TweetWatchVideoTask, TweetWatchVideoTaskAdmin)
admin_tasks.register(models.TweetTask, TweetTaskAdmin)


admin_platform_tasks.register(models.ProfileFollowTask, ProfileFollowTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.TweetRepostTask, TweetRepostTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.TweetLikeTask, TweetLikeTaskPlatformAdmin)
admin_platform_tasks.register(models.TweetCommentExactTask, TweetCommentExactTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.TweetCommentTask, TweetCommentTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.TweetWatchVideoTask, TweetWatchVideoTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.TweetTask, TweetTaskPlatformAdmin)
