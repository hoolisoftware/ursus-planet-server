from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .. import models


class TaskCustomLogSerializer(ModelSerializer):
    class Meta:
        model = models.TaskCustomLog
        fields = "__all__"


class UserTaskCustomSerializer(ModelSerializer):
    log = SerializerMethodField(method_name='get_log')

    class Meta:
        model = models.TaskCustom
        fields = "__all__"

    def get_log(self, instance):
        if self.context.get('request').user:
            return TaskCustomLogSerializer(
                models.TaskCustomLog.objects.filter(
                    user=self.context.get('request').user,
                    task=instance.id).first()
            ).data
        else:
            return None
