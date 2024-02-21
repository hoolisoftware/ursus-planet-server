from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ..models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserReferralSerializer(ModelSerializer):
    wallets = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='hash'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'wallets'
        ]
