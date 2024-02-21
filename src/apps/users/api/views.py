from random import randint

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from .. import models
from . import serializers
from . import exceptions


User = get_user_model()


class UserSelfMixin:

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return User.objects.filter(id=self.request.user.id).first()


class UserViewSet(UserSelfMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer


class UserReferralsListAV(ListAPIView):
    serializer_class = serializers.UserReferralSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.referrals.all()


class UserSetReferrerAV(APIView):

    def post(self, request):
        username = request.data.get('username')

        if request.user.referrer:
            raise exceptions.ReferrerAlreadySet

        if not username:
            raise exceptions.ReferrerUsernameNotProvided

        user = User.objects.filter(username=username).first()
        if not user:
            raise exceptions.ReferrerUsernameInvalid

        if not user.referrer:
            raise exceptions.ReferrerInvalid

        if user.referral_quote <= 0:
            raise exceptions.ReferrerQuoteExceeded

        request.user.referrer = user
        request.user.save()
        user.referral_quote -= 1
        user.save()

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
