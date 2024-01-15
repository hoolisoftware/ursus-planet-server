from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')

urlpatterns = [
    path('update-username-email/', views.UserUpdateUsernameEmailView.as_view())
] + router.urls