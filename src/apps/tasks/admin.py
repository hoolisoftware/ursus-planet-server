from django.contrib import admin
from django.contrib.admin import AdminSite

from apps.projects.models import Project
from apps.projects.admin import ProjectAdmin
from apps.users.models import User
from apps.users.admin import UserAdmin

from . import models


LIST_DISPLAY_COMMON = [
    'project',
    'created'
]


class TaskAdminSite(AdminSite):
    site_header = "Ursas Planet tasks admin panel"
    site_title = "Ursas Planet tasks admin panel"


class TaskAdmin(admin.ModelAdmin):
    autocomplete_fields = ('project',)


class ProjectProxyAdmin(ProjectAdmin):
    exclude = ('owner',)
    autocomplete_fields = []


admin_tasks = TaskAdminSite(name='admin_tasks')


admin_tasks.register(models.ProjectProxy, ProjectProxyAdmin)