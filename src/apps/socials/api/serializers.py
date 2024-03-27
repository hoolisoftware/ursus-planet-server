from rest_framework.serializers import ModelSerializer

from ..models import SocialAccountsOfCompany


class SocialAccountsOfCompanySerializer(ModelSerializer):
    class Meta:
        model = SocialAccountsOfCompany
        fields = '__all__'
