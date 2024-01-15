from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView

from .. import models
from . import serializers


User = get_user_model()


class UserSelfMixin:

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


    def get_object(self):
        return User.objects.filter(id=self.request.user.id).first()


class UserViewSet(UserSelfMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer
