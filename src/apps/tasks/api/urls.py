from django.urls import path

from . import views


urlpatterns = (
    path('settings/', views.TaskSettingsRetrieveAV.as_view()),
)
