from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from . import serializers
from . import exceptions
from .. import models
from .. import utils


class PlatformTasksRetieveAV(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        settings = models.PlatformTaskSettings.load()
        logs = models.PlatformTaskLog.objects.filter(user=request.user)
        return Response((
            {
                "name": task.name,
                **{
                    attr[0]: getattr(
                        settings,
                        f'{task.name}_{attr[0]}',
                        None
                    ) for attr in utils.get_tasks_platform_attrs()
                },
                "log": serializers.PlatformTaskLogSerializer(
                    logs.filter(task=task.name).first()
                ).data
            } for task in utils.get_tasks_platform()
        ))


class PlatformTasksSettingsAV(RetrieveAPIView):
    serializer_class = serializers.PlatformTaskSettingsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return models.PlatformTaskSettings.load()


class PlatformTaskGetRewardAV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        task_name = request.data.get('task_name')

        if task_name not in (task.name for task in utils.get_tasks_platform()):
            raise exceptions.InvalidTaskName

        task_log = models.PlatformTaskLog.objects.filter(
            user=request.user,
            task=task_name
        ).first()

        if not task_log:
            raise exceptions.NotFoundTaskLog

        if task_log.got:
            raise exceptions.AlreadyGotReward

        request.user.add_points(task_log.reward)
        task_log.got = True
        task_log.save()

        return Response({"status": "ok"})


class ReferrerClaimAV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.points += request.user.points_referral
        request.user.points_referral = 0
        request.user.save()

        return Response({"status": "ok"})
