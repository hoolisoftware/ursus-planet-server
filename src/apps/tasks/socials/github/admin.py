from apps.tasks.admin import (
    TaskAdmin,
    TaskPlatformAdmin,
    admin_tasks,
    admin_platform_tasks
)

from . import models


class ProfileFollowTaskAdmin(TaskAdmin):
    pass


class RepositoryStarTaskAdmin(TaskAdmin):
    pass


class RepositoryForkTaskAdmin(TaskAdmin):
    pass


class ProfileFollowTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class RepositoryStarTaskPlatformAdmin(TaskPlatformAdmin):
    pass


class RepositoryForkTaskPlatformAdmin(TaskPlatformAdmin):
    pass


admin_tasks.register(models.ProfileFollowTask, ProfileFollowTaskAdmin)
admin_tasks.register(models.RepositoryStarTask, RepositoryStarTaskAdmin)
admin_tasks.register(models.RepositoryForkTask, RepositoryForkTaskAdmin)

admin_platform_tasks.register(models.ProfileFollowTask, ProfileFollowTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.RepositoryStarTask, RepositoryStarTaskPlatformAdmin)  # NOQA
admin_platform_tasks.register(models.RepositoryForkTask, RepositoryForkTaskPlatformAdmin)  # NOQA
