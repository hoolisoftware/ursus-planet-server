from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import exceptions
from .. import models


class PlatformTasksRetieveAV(APIView):

    def get(self, request):
        settings = models.PlatformTaskSettings.load()
        logs = models.PlatformTaskLog.objects.filter(user=request.user)
        return Response((
            {
                "name": task[0],
                **{
                    setting[0]: getattr(
                        settings,
                        f'{task[0]}_{setting[0]}',
                        None
                    ) for setting in models.TASK_SETTINGS
                },
                "log": serializers.PlatformTaskLogSerializer(logs.filter(task=task[0]).first()).data  # NOQA
            } for task in models.TASKS
        ))


class PlatformTaskGetRewardAV(APIView):

    def post(self, request):
        task_name = request.data.get('task_name')

        if task_name not in [task[0] for task in models.TASKS]:
            raise exceptions.InvalidTaskName

        task_log = models.PlatformTaskLog.objects.filter(
            user=request.user,
            task=task_name
        ).first()

        if not task_log:
            raise exceptions.NotFoundTaskLog

        if task_log.got:
            raise exceptions.AlreadyGotReward

        request.user.points += task_log.reward
        request.user.save()
        task_log.got = True
        task_log.save()

        return Response({"status": "ok"})
