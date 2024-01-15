from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.tokens import RefreshToken

from apps.wallets.models import UserWallet, Chain


User = get_user_model()


@csrf_exempt
def auth_view(request) -> JsonResponse:
    chain_id = request.GET.get('chain_id')
    address = request.GET.get('address')

    if not (chain_id and address):
        return JsonResponse({'error': 'please provide "chain id" and "address" in the POST body'})

    chain = Chain.objects.filter(chain_id=chain_id).first() 
    wallet = UserWallet.objects.filter(hash=address).first()
    user = None

    if not chain:
        chain = Chain.objects.create(chain_id=chain_id)

    if not wallet:
        user = User.objects.create()
        user.username = f'user{user.id}'
        user.save()
        wallet = UserWallet.objects.create(hash=address, chain=chain, user=user)

    if not user:
        user = User.objects.filter(wallets=wallet).first()

    refresh = RefreshToken.for_user(user)

    return JsonResponse({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })