from rest_framework.serializers import ModelSerializer

from ..models import TaskSettings


class TaskSettingsSerializer(ModelSerializer):
    class Meta:
        model = TaskSettings
        fields = "__all__"
