from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .. import models


class PlatformTasksSettingsRetrieveAV(RetrieveAPIView):

    serializer_class = serializers.PlatformTasksSettingsSerializer
    model = models.PlatformTasksSettings

    def get_object(self):
        return self.model.load()


class PlatformTasksLogsRetrieveAV(APIView):

    def get(self, request):
        return Response({
            "task_social_x" : serializers.TaskSocialXLogSerializer(models.TaskSocialXLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_social_github" : serializers.TaskSocialGithubLogSerializer(models.TaskSocialGithubLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_social_discord" : serializers.TaskSocialDiscordLogSerializer(models.TaskSocialDiscordLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_social_telegram" : serializers.TaskSocialTelegramLogSerializer(models.TaskSocialTelegramLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_email" : serializers.TaskEmailLogSerializer(models.TaskEmailLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_username" : serializers.TaskUsernameLogSerializer(models.TaskUsernameLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_domain_id" : serializers.TaskDomainIdLogSerializer(models.TaskDomainIdLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_avatar" : serializers.TaskAvatarLogSerializer(models.TaskAvatarLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_nft_avatar" : serializers.TaskNftAvatarLogSerializer(models.TaskNftAvatarLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_ursas_collection_nft_avatar" : serializers.TaskUrsasCollectionNftAvatarLogSerializer(models.TaskUrsasCollectionNftAvatarLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_wallet" : serializers.TaskWalletLogSerializer(models.TaskWalletLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_chain" : serializers.TaskChainLogSerializer(models.TaskChainLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_referral_self" : serializers.TaskReferralSelfLogSerializer(models.TaskReferralSelfLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_email_notification" : serializers.TaskEmailNotificationLogSerializer(models.TaskEmailNotificationLog.objects.filter(user=request.user).first()).data,  # NOQA
            "task_cabinet_notification" : serializers.TaskCabinetNotificationLogSerializer(models.TaskCabinetNotificationLog.objects.filter(user=request.user).first()).data  # NOQA
        })
