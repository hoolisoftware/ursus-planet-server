from rest_framework.serializers import ModelSerializer

from ..models import PlatformTasksSettings


class PlatformTasksSettingsSerializer(ModelSerializer):
    class Meta:
        model = PlatformTasksSettings
        fields = '__all__'
