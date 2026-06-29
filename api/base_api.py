import requests
from data.endpoints import BASE_URL


class BaseApi:

    def post(self, endpoint, payload=None, headers=None):
        return requests.post(
            f"{BASE_URL}{endpoint}",
            json=payload,
            headers = headers
        )

    def get(self, endpoint, headers=None):
        return requests.get(
            f"{BASE_URL}{endpoint}",
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return requests.delete(
            f"{BASE_URL}{endpoint}",
            headers=headers
        )

    def patch(self, endpoint, payload=None, headers=None):
        return requests.patch(
            f"{BASE_URL}{endpoint}",
            data=payload,
            headers=headers
        )
