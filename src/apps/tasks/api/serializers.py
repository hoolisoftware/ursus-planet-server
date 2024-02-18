from rest_framework.serializers import ModelSerializer

from .. import models


class PlatformTasksSettingsSerializer(ModelSerializer):
    class Meta:
        model = models.PlatformTasksSettings
        fields = '__all__'


class TaskSocialXLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskSocialXLog
        fields = '__all__'


class TaskSocialGithubLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskSocialGithubLog
        fields = '__all__'


class TaskSocialDiscordLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskSocialDiscordLog
        fields = '__all__'


class TaskSocialTelegramLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskSocialTelegramLog
        fields = '__all__'


class TaskEmailLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskEmailLog
        fields = '__all__'


class TaskUsernameLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskUsernameLog
        fields = '__all__'


class TaskDomainIdLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskDomainIdLog
        fields = '__all__'


class TaskAvatarLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskAvatarLog
        fields = '__all__'


class TaskNftAvatarLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskNftAvatarLog
        fields = '__all__'


class TaskUrsasCollectionNftAvatarLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskUrsasCollectionNftAvatarLog
        fields = '__all__'


class TaskWalletLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskWalletLog
        fields = '__all__'


class TaskChainLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskChainLog
        fields = '__all__'


class TaskReferralSelfLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskReferralSelfLog
        fields = '__all__'


class TaskEmailNotificationLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskEmailNotificationLog
        fields = '__all__'


class TaskCabinetNotificationLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskCabinetNotificationLog
        fields = '__all__'
