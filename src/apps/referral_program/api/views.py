from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.referral_program.models import ReferralProgramSettings

from . import serializers
from . import utils
from .. import models


User = get_user_model()


class ReferralProgramSettingsRetrieveAV(RetrieveAPIView):
    serializer_class = serializers.ReferralProgramSettingsSerializer

    def get_object(self):
        return models.ReferralProgramSettings.load()


class ReferralProgramLeaderboardListAV(ListAPIView):
    serializer_class = serializers.UserReferrerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        settings = ReferralProgramSettings.load()

        return User.objects\
            .annotate(referrals_count=Count('referrals'))\
            .order_by('-referrals_count')\
            .filter(referrals_count__gt=0)\
            .exclude(username=getattr(settings.referral_genesis_user, 'username', None))  # NOQA


class UserSetReferrerCookie(APIView):

    def post(self, request):
        response = Response()
        response.set_cookie(
            key=settings.REFERRER_COOKIE['COOKIE'],
            value=request.data.get('username'),
            expires=settings.REFERRER_COOKIE['LIFETIME'],
            secure=settings.REFERRER_COOKIE['SECURE'],
            httponly=settings.REFERRER_COOKIE['HTTP_ONLY'],
            samesite=settings.REFERRER_COOKIE['SAMESITE'],
        )
        response.data = {'success': 'ok'}
        return response


class UserSetReferrerAV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        utils.set_user_referrer(
            user=request.user,
            referrer_username=request.data.get('username')
        )

        return Response({'status': 'ok'})


class UserClaimAV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.points += request.user.points_referrer
        request.user.points_referrer = 0
        request.user.save()

        return Response({"status": "ok"})
