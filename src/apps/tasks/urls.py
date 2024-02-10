from django.urls import path

from .admin import admin_tasks


urlpatterns = (
    path('', admin_tasks.urls),
)