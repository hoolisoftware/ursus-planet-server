from django.urls import path

from . import views


urlpatterns = (
    path('', views.SocialsUserAV.as_view()),
    path('authorize/', views.SocialsAuthorizeAV.as_view()),
)