from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    IntegerField
)

from ..models import User


class UserSerializer(ModelSerializer):
    read_only_fields = (
        'is_active',
        'is_staff',
        'referrer',
        'referral_points,'
        'points',
        'color1',
        'color2',
        'color3',
        'color4',
        'color5'
    )
    referrer = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    referral_count = IntegerField()

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
            'wallets',
            'referral_count'
        ]
