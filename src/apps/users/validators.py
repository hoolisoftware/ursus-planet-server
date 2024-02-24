from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


username_validator = RegexValidator(
    regex=r'^[A-Za-z]{1}[\w.@+-]{4,15}\Z$',
    message=(
        "Enter a valid username. This value may contain only letters, "  # NOQA
        "numbers, and @/./+/-/_ characters, start from letter, and have length between 4 and 16 characters."  # NOQA
    )
)


def username_forbidden_validator(username: str) -> None:
    usernames_now_allowed = (
        'unknown',
        'ursas',
        'ursasplanet',
        'ursas_planet',
        'teddy',
        'teddy_ursas',
        'teddy_ar',
        'teddy_arr',
        'teddy_arrr',
    )
    if username in usernames_now_allowed:
        raise ValidationError("This username isn't allowed")


def avatar_validator(avatar) -> None:
    if avatar:
        if avatar.size > 5*1024*1024:
            raise ValidationError("Avatar image must be small than 5 mb")
