from rest_framework.viewsets import ModelViewSet

from .. import models
from . import serializers

class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer