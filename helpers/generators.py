import random
import string


def generate_user():
    suffix = ''.join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=8
        )
    )

    return {
        "email": f"test_{suffix}@yandex.ru",
        "password": "Password123",
        "name": f"user_{suffix}"
    }
