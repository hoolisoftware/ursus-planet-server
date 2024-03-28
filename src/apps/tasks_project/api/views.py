from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

        if not (task_log := models.TaskCustomLog.objects.filter(task=task_id).first()):  # noqa
            raise exceptions.InvalidTaskIdException

        return task_log


class TaskCustomCheckAV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not (task_id := self.request.data.get('task_id')):
            raise exceptions.MissingTaskIdException

        if not (task := models.TaskCustom.objects.filter(id=task_id).first()):
            raise exceptions.InvalidTaskIdException

        models.TaskCustomLog.objects.update_or_create(
            task=task,
            reward=task.reward,
            user=request.user
        )

        return Response({"success": "ok"})
