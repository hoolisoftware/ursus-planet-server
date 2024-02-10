from django.contrib import admin
from django.contrib.admin import AdminSite

from . import models


class TaskAdminSite(AdminSite):
    site_header = "Ursas Planet tasks admin panel"
    site_title = "Ursas Planet tasks admin panel"


admin_tasks = TaskAdminSite(name='admin_tasks')