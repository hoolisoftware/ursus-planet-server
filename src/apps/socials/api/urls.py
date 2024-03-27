from django.urls import path

from . import views


urlpatterns = (
    path('', views.SocialsUserAV.as_view()),
    path('social-accounts-of-company/', views.SocialAccountsOfCompanyAV.as_view()),  # noqa
    path('authorize/', views.SocialsAuthorizeAV.as_view()),
    path('config/', views.SocialsConfigAV.as_view()),
    path('telegram/callback/', views.TelegramCallbackAV.as_view())
)
