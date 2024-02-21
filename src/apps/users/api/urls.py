from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')

urlpatterns = [
    path('email-change/', views.UserChangeEmail.as_view()),
    path('email-verify/', views.UserVerifyEmail.as_view()),
    path('referrals/', views.UserReferralsListAV.as_view()),
    path('referrer/set/', views.UserSetReferrerAV.as_view())
] + router.urls
