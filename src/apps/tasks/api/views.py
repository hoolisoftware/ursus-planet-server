from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from . import serializers
from . import exceptions
from .. import models


class PlatformTasksRetieveAV(APIView):
    permission_classes = [IsAuthenticated]

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


class PlatformTasksSettingsAV(RetrieveAPIView):
    serializer_class = serializers.PlatformTaskSettingsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return models.PlatformTaskSettings.load()


class PlatformTaskGetRewardAV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        settings = models.PlatformTaskSettings.load()
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
        if request.user.referrer:
            request.user.referrer.points_referral += task_log.reward * (settings.referral_comission / 100)  # NOQA
            request.user.referrer.save()

        return Response({"status": "ok"})
