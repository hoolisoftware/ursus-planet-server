from django.urls import path

from . import views


urlpatterns = (
    path('platform/', views.PlatformTasksRetieveAV.as_view()),
    path('platform/get_reward/', views.PlatformTaskGetRewardAV.as_view())
)
