from rest_framework.generics import RetrieveAPIView

from . import serializers
from ..models import PlatformTasksSettings


class PlatformTasksSettingsRetrieveAV(RetrieveAPIView):

    serializer_class = serializers.PlatformTasksSettingsSerializer
    model = PlatformTasksSettings

    def get_object(self):
        return self.model.load()
