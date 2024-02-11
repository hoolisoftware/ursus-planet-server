from django.urls import path

from .admin import admin_tasks, admin_platform_tasks


urlpatterns = (
    path('platform/', admin_platform_tasks.urls),
    path('', admin_tasks.urls),
)