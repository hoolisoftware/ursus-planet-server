from django.db.models import Model
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from django.conf import settings
from urllib.parse import urlparse
import requests
import orjson

from core.utils import to_base64
from .. import models
from . import exceptions
from . import utils


SUPPORTED_SOCIALS = [
    'github',
    'discord',
    'x',
    'telegram'
]


class TelegramCallbackAV(views.APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        uuid = request.data.get('uuid')

        if models.SocialAccountTelegram.objects.filter(username=username).first():
            raise exceptions.AccountAlreadyTaken

        if not request.data.get('token') == settings.TELEGRAM_BOT_TOKEN:
            raise exceptions.BotTokenNotProvided

        if not username and not uuid:
            raise exceptions.UUIDnUsernameNotProvided

        if object := models.SocialAccountTelegramCode.objects.filter(username=username).first():
            object.uuid = uuid
            object.save()
        else: 
            models.SocialAccountTelegramCode.objects.create(
                username=request.data.get('username'),
                uuid=request.data.get('uuid')
            )

        return Response({'status': 'ok'})


class SocialsConfigAV(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "discord": {
                "client_id": settings.DISCORD_CLIENT_ID,
                "redirect_uri": settings.DISCORD_REDIRECT_URI
            },
            "github": {
                "client_id": settings.GITHUB_CLIENT_ID,
                "redirect_uri": settings.GITHUB_REDIRECT_URI
            },
            "x": {
                "client_id": settings.X_CLIENT_ID,
                "redirect_uri": settings.X_REDIRECT_URI
            }
        })


class SocialsUserAV(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return Response({
            'github': getattr(models.SocialAccountGithub.objects.filter(owner=user).first(), 'username', None),
            'telegram': getattr(models.SocialAccountTelegram.objects.filter(owner=user).first(), 'username', None),
            'discord': getattr(models.SocialAccountDiscord.objects.filter(owner=user).first(), 'username', None),
            'x': getattr(models.SocialAccountX.objects.filter(owner=user).first(), 'username', None)
        })

class SocialsAuthorizeAV(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:

        if not (code := request.data.get('code')):
            raise exceptions.CodeNotProvided

        if not (social := request.data.get('social')):
            raise exceptions.SocialNotProvided

        if not social in SUPPORTED_SOCIALS:
            raise exceptions.SocialNotProvided

        if social == 'github':
            self._create_or_update_account(utils.get_github_username(code), models.SocialAccountGithub)
        elif social == 'discord':
            self._create_or_update_account(utils.get_discord_username(code), models.SocialAccountDiscord)            
        elif social == 'x':
            self._create_or_update_account(utils.get_x_username(code), models.SocialAccountX)            
        elif social == 'telegram':
            self._create_or_update_telegram_account(uuid=code)

        return Response({'status': 'ok'})

    def delete(self, request) -> Response:

        if not (social := request.data.get('social')):
            raise exceptions.SocialNotProvided
        
        if not social in SUPPORTED_SOCIALS:
            raise exceptions.SocialNotProvided

        if social == 'github':
            account_model = models.SocialAccountGithub
        elif social == 'discord':
            account_model = models.SocialAccountDiscord
        elif social == 'x':
            account_model = models.SocialAccountX
        elif social == 'telegram':
            account_model = models.SocialAccountTelegram

        if object := account_model.objects.filter(owner=self.request.user).first():
            object.delete()
            return Response({'status': 'ok'})

        raise exceptions.AccountNotFound


    def _create_or_update_account(self, username: str, account_model: Model) -> None:
        if account := account_model.objects.filter(owner=self.request.user).first():
            account.username = username
            account.save()
        elif account_model.objects.filter(username=username):
            raise exceptions.AccountAlreadyTaken
        else:
            account_model.objects.create(
                username=username,
                owner=self.request.user
            )

    def _create_or_update_telegram_account(self, uuid: str) -> None:
        if not (object := models.SocialAccountTelegramCode.objects.filter(uuid=uuid).first()):
            raise exceptions.UUIDInvalid

        username = object.username
        object.delete()

        if object := models.SocialAccountTelegram.objects.filter(owner=self.request.user):
            object.delete()

        models.SocialAccountTelegram.objects.create(
            username=username,
            owner=self.request.user
        )
