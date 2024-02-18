from django.urls import path

from . import views


urlpatterns = (
    path('platform/', views.PlatformTasksSettingsRetrieveAV.as_view()),
)
