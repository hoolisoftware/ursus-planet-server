from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from apps.wallets.models import UserWallet, Chain
from .utils import get_or_create_user 

from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf

from apps.wallets.models import UserWallet, Chain


User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
        
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    authentication_classes = []

    def post(self, request, format=None) -> Response:

        data = request.data

        if not (
            (chain_id := data.get('chain_id')) and
            (address := data.get('address'))
        ):
            return Response({'error': 'please provide "chain id" and "address" in the POST body'})

        user = get_or_create_user(
            chain_id,
            address
        )

        print(user)
        if user.is_active:
            response = Response()
            data = get_tokens_for_user(user)
            response.set_cookie(
                key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                value = data["access"],
                expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = {"detail": "OK", "data": data}
            return response
        else:
            return Response({"detail": "This account is not active!"}, status=status.HTTP_404_NOT_FOUND)


User = get_user_model()
