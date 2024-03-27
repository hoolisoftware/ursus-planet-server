from django.apps import AppConfig


class TasksPlatformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tasks_platform'
    verbose_name = 'Tasks of platform'

    def ready(self):
        from . import signals  # NOQA
