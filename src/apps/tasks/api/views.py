from abc import ABC, abstractmethod
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from apps.tasks.models import TaskLog
from . import exceptions


class TaskGetRewardAV(APIView, ABC):
    permission_classes = [IsAuthenticated]

    @abstractmethod
    def get_log_or_none(self) -> TaskLog:
        pass

    def post(self, request) -> Response:

        log = self.get_log_or_none()

        if not log:
            raise exceptions.NotFoundTaskLog

        log.withdraw_points()
        return Response({"status": "ok"})
