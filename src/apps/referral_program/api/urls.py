from django.urls import path

from . import views


urlpatterns = (
    path('settings/', views.ReferralProgramSettingsRetrieveAV.as_view()),
    path('leaderboard/', views.ReferralProgramLeaderboardListAV.as_view()),
    path('me/set-referrer/', views.UserSetReferrerAV.as_view()),
    path('me/set-referrer-cookie/', views.UserSetReferrerCookie.as_view()),
    path('me/claim/', views.UserClaimAV.as_view())
)
