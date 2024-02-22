import random


def random_hex() -> str:
    return f"#{hex(random.randrange(0, 2**24))[2:]}".replace("/F(?=[A-F0-9](?:[A-F0-9]{2}){0,2}$)/g", "E")  # NOQA


def default_referral_quote() -> int:
    from apps.tasks.models import PlatformTaskSettings

    return PlatformTaskSettings.load().referral_quote
