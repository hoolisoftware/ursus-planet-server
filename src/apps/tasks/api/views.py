from rest_framework.generics import RetrieveAPIView

from . import serializers
from .. import models


class TaskSettingsRetrieveAV(RetrieveAPIView):
    serializer_class = serializers.TaskSettingsSerializer

    def get_object(self):
        return models.TaskSettings.load()
