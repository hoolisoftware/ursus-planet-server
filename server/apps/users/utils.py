import random


def random_hex() -> str:
    return f"#{hex(random.randrange(0, 2**24))[2:]}"