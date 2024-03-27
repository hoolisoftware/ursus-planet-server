from django.contrib.auth import get_user_model

from . import exceptions


User = get_user_model()


def set_user_referrer(user: User, referrer_username: str) -> None:
    if user.referrer:
        raise exceptions.ReferrerAlreadySet

    if not referrer_username:
        raise exceptions.ReferrerUsernameNotProvided

    referrer_user = User.objects.filter(username=referrer_username).first()
    if not referrer_user:
        raise exceptions.ReferrerUsernameInvalid

    if not referrer_user.referrer:
        raise exceptions.ReferrerInvalid

    if referrer_user.referral_quote <= 0:
        raise exceptions.ReferrerQuoteExceeded

    user.referrer = referrer_user
    user.save()
    referrer_user.referral_quote -= 1
    referrer_user.save()
