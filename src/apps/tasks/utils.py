from typing import Callable

from .tasks_platform import Task
from .settings import (
    INSTALLED_TASKS_PLATFORM,
    INSTALLED_TASKS_PLATFORM_ATTRS
)


def get_tasks_platform() -> list[Task]:
    return INSTALLED_TASKS_PLATFORM


def get_tasks_platform_attrs() -> tuple[str, Callable]:
    return INSTALLED_TASKS_PLATFORM_ATTRS
