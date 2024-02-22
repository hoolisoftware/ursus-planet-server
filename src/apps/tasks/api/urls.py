from django.urls import path

from . import views


urlpatterns = (
    path('platform/settings/', views.PlatformTasksSettingsAV.as_view()),
    path('platform/get_reward/', views.PlatformTaskGetRewardAV.as_view()),
    path('platform/', views.PlatformTasksRetieveAV.as_view()),
    path('referrer/claim/', views.ReferrerClaimAV.as_view())
)
