from rest_framework.generics import ListAPIView

from apps.tasks.api.views import TaskGetRewardAV
from .. import models
from . import serializers
from . import exceptions


class UserTaskCustomListAV(ListAPIView):
    serializer_class = serializers.UserTaskCustomSerializer

    def get_queryset(self):
        return models.TaskCustom.objects.all()


class TaskCustomGetRewardAV(TaskGetRewardAV):

    def get_log_or_none(self) -> models.TaskCustomLog:
        if not (task_id := self.request.data.get('task_id')):
            raise exceptions.MissingTaskIdException

        if not (task_log := models.TaskCustomLog.objects.filter(id=task_id).first()):  # noqa
            raise exceptions.InvalidTaskIdException

        return task_log
