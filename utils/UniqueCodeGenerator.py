from django.utils import timezone
import hashlib
import random


def generate_key(text: str, size: int = 10) -> str:
    return hashlib.md5(str(text + str(timezone.now())).encode()).hexdigest()[:size]


def generate_random_number(length: int) -> str:
    final = ""
    if length > 0:
        for i in range(0, length):
            final = final + str(random.randint())
    return final
