import base64


def to_base64(value: str) -> str:
    return base64.b64encode(value.encode('ascii')).decode('ascii')
