from random import randint

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.tasks.models import PlatformTaskSettings
from .. import models
from . import serializers
from . import exceptions
from . import utils


User = get_user_model()


class UserSelfMixin:

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return User.objects.filter(id=self.request.user.id).first()


class UserViewSet(UserSelfMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer


class UserSelfReferralsListAV(ListAPIView):
    serializer_class = serializers.UserReferralSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        settings = PlatformTaskSettings.load()

        return self.request.user.referrals\
            .annotate(referrals_count=Count('referrals'))\
            .order_by('-referrals_count')\
            .filter(referrals_count__gt=0)\
            .exclude(username=getattr(settings.referral_genesis_user, 'username', None))  # NOQA


class UserReferralsListAV(ListAPIView):
    serializer_class = serializers.UserReferralSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        settings = PlatformTaskSettings.load()

        return User.objects\
            .annotate(referrals_count=Count('referrals'))\
            .order_by('-referrals_count')\
            .filter(referrals_count__gt=0)\
            .exclude(username=getattr(settings.referral_genesis_user, 'username', None))  # NOQA


class UserSetReferralCookie(APIView):

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


class UserChangeEmail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if not (email := request.data.get('email')):
            raise exceptions.EmailNotProvidedException

        if User.objects.filter(email=email):
            raise exceptions.EmailAlreadyTaken

        if object := models.UserEmailCode.objects.filter(user=request.user):
            object.delete()

        object = models.UserEmailCode.objects.create(
            user=request.user,
            code=''.join([str(randint(1, 9)) for _ in range(6)]),
            email=email
        )

        send_mail(
            subject="Ursas email verification",
            from_email='support@ursasplanet.com',
            html_message=render_to_string('email-verify.html', {'code': object.code}),  # NOQA
            message=render_to_string('email-verify.txt', {'code': object.code}),  # NOQA
            recipient_list=[object.email],
            fail_silently=False,
        )

        return Response({'success': 'ok'})


class UserVerifyEmail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if not (code := request.data.get('code')):
            raise exceptions.CodeNotProvided

        if not (object := models.UserEmailCode.objects.filter(code=code, user=request.user).first()):  # NOQA
            raise exceptions.BadCodeProvided

        request.user.email = object.email
        request.user.save()
        object.delete()

        return Response({'success': 'ok'})
