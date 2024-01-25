from django.db.models import Model
from rest_framework import views
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
    'x'
]


class SocialsUserAV(views.APIView):
    def get(self, request):
        user = self.request.user
        return Response({
            'github': getattr(models.SocialAccountGithub.objects.filter(owner=user).first(), 'username', None),
            'telegram': getattr(models.SocialAccountTelegram.objects.filter(owner=user).first(), 'username', None),
            'discord': getattr(models.SocialAccountDiscord.objects.filter(owner=user).first(), 'username', None),
            'x': getattr(models.SocialAccountX.objects.filter(owner=user).first(), 'username', None)
        })

class SocialsAuthorizeAV(views.APIView):

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

        return Response({'status': 'ok'})

    def delete(self, request) -> Response:

        print(request.data)

        if not (social := request.data.get('social')):
            raise exceptions.SocialNotProvided
        
        if not social in SUPPORTED_SOCIALS:
            raise exceptions.SocialNotProvided

        if social == 'github':
            account_model = models.SocialAccountGithub
        elif social == 'discord':
            account_model = models.SocialAccountDiscord

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
