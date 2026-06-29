import pytest

from api.user_api import UserApi
from helpers.generators import generate_user

@pytest.fixture
def authorized_user():

    user_api = UserApi()

    user_data = generate_user()

    create_response = user_api.create_user(user_data)

    access_token = create_response.json()['accessToken']

    yield {
        'user': user_data,
        'token': access_token
    }

    user_api.delete_user(access_token)

@pytest.fixture
def cleanup_user():
     user_token = []

     yield user_token 
    
     user_api = UserApi()

     for token in user_token:
        user_api.delete_user(token)
