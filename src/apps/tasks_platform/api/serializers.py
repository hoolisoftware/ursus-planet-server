from rest_framework.serializers import ModelSerializer

from .. import models


class PlatformTaskLogSerializer(ModelSerializer):
    class Meta:
        model = models.PlatformTaskLog
        fields = '__all__'
