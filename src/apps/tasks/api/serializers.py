from rest_framework.serializers import ModelSerializer

from .. import models


class PlatformTaskSettingsSerializer(ModelSerializer):
    class Meta:
        model = models.PlatformTaskSettings
        fields = '__all__'


class PlatformTaskLogSerializer(ModelSerializer):
    class Meta:
        model = models.PlatformTaskLog
        fields = '__all__'
