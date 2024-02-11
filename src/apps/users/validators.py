from django.core.validators import RegexValidator


username_validator = RegexValidator(
    regex=r'^[A-Za-z]{1}[\w.@+-]{4,15}\Z$',
    message=(
        "Enter a valid username. This value may contain only letters, "  # NOQA
        "numbers, and @/./+/-/_ characters, start from letter, and have length between 4 and 16 characters."  # NOQA
    )
)
