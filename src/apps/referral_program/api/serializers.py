from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .. import models


User = get_user_model()


class ReferralProgramSettingsSerializer(ModelSerializer):
    class Meta:
        model = models.ReferralProgramSettings
        fields = "__all__"


class UserReferrerSerializer(ModelSerializer):
    wallets = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='hash'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'wallets',
            'referral_count'
        ]
