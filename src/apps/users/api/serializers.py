from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ..models import User


class UserSerializer(ModelSerializer):
    read_only_fields = ('is_active', 'is_staff', 'referrer')
    referrer = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

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
