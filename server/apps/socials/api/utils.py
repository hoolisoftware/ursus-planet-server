from django.conf import settings

import requests
import orjson

from core.utils import to_base64
from . import exceptions


def get_x_username(code: str) -> str :

    # access token request with given code
    response_access_token = requests.post(
        'https://api.twitter.com/2/oauth2/token',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {str(to_base64(f"{settings.X_CLIENT_ID}:{settings.X_CLIENT_SECRET}"))}'
        },
        data={
            'grant_type': 'authorization_code',
            'redirect_uri': settings.X_REDIRECT_URI,
            'code_verifier': 'challenge',
            'code': code
        }
    )
    print(to_base64(f"{settings.X_CLIENT_ID}:{settings.X_CLIENT_SECRET}"))

    if 'error' in response_access_token.text:
        raise exceptions.BadCodeProvided    

    # user request with requested access token 
    response_user = requests.get('https://api.twitter.com/2/users/me', headers={
        'Authorization': f'Bearer {orjson.loads(response_access_token.text)["access_token"]}',
    })

    if response_user.status_code >= 401 and response_user.status_code < 500:
            raise exceptions.SomethingWentWrong

    return orjson.loads(response_user.text)['data']['username']


def get_github_username(code: str) -> str :

    # access token request with given code
    response_access_token = requests.post(
        'https://github.com/login/oauth/access_token',
        data={
            'client_id': settings.GITHUB_CLIENT_ID,
            'client_secret': settings.GITHUB_SECRET_KEY,
            'code': code
        }
    )

    if 'error' in response_access_token.text:
        raise exceptions.BadCodeProvided    

    # user request with requested access token 
    response_user = requests.get('https://api.github.com/user', headers={
        'Authorization': f'Bearer {response_access_token.text.split("&")[0].split("=")[1]}',
    })

    if response_user.status_code == 401:
        raise exceptions.SomethingWentWrong

    return orjson.loads(response_user.text)['login']


def get_discord_username(code: str) -> str :

    # access token request with given code
    response_access_token = requests.post(
        'https://discord.com/api/oauth2/token',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        data={
            'grant_type': 'authorization_code',
            'redirect_uri': settings.DISCORD_REDIRECT_URI,
            'client_id': settings.DISCORD_CLIENT_ID,
            'client_secret': settings.DISCORD_SECRET_KEY,
            'code': code,
        }
    )

    if 'error' in response_access_token.text:
        raise exceptions.BadCodeProvided    

    # user request with requested access token
    response_user = requests.get(
        'https://discord.com/api/users/@me',
        headers={
            'Authorization': f'Bearer {orjson.loads(response_access_token.text)["access_token"]}',
        }
    )

    if response_user.status_code == 401:
        raise exceptions.SomethingWentWrong

    return orjson.loads(response_user.text)['username']