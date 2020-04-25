from random import randint
from django.core.cache import cache


def verify(key: str, value: str, release_key_on_success: bool = True) -> bool:
    """ Validate given value match what we generated on django cache
        Successful validation will delete the key if release_key_on_success is True
    """

    if cache.get(get_key(key)) == value:
        if release_key_on_success:
            delete(key)

        return True
    return False


def create(key: str, expiry: int = 600, length: int = 4) -> str:
    otp = ''.join(["{}".format(randint(0, 9)) for num in range(1, length)])
    cache.set(get_key(key), otp, expiry)
    return otp


def delete(key: str) -> None:
    cache.delete(get_key(key))


def get_key(key: str) -> str:
    return f"django_otp_cache:{key}"
