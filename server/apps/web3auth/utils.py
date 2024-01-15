from django.contrib.auth import get_user_model

from apps.wallets.models import UserWallet, Chain


User = get_user_model()


def get_or_create_user(chain_id: str, address: str) -> User:

    chain = Chain.objects.filter(chain_id=chain_id).first() 
    wallet = UserWallet.objects.filter(hash=address, chain=chain).first()
   
    if not chain:
        chain = Chain.objects.create(chain_id=chain_id)

    if not wallet:
        user = User.objects.create()
        user.save()
        wallet = UserWallet.objects.create(hash=address, chain=chain, user=user)

        return user

    return wallet.user

