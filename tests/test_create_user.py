from api.user_api import UserApi
from helpers.generators import generate_user
from data.message_error import ERROR_USER_ALREADY_EXISTS, ERROR_REQUIRED_FIELDS
import pytest
import allure

class TestCreateUser:
    @allure.title('Тест: Cоздание уникального пользователя с корректным логином, паролем и именем')
    def test_create_user_unique(self, cleanup_user):

        user_data = generate_user()

        user_api = UserApi() 

        response = user_api.create_user(user_data)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] == True

        cleanup_user.append(body["accessToken"])
    @allure.title('Тест: Создание уже существующего пользователя')
    def test_create_user_exist(self, cleanup_user):

        user_data = generate_user()

        user_api = UserApi() 

        response = user_api.create_user(user_data)
        response_2 = user_api.create_user(user_data)
        body = response.json()
        body_2 = response_2.json()

        assert response_2.status_code == 403
        assert body_2["message"] == ERROR_USER_ALREADY_EXISTS

        cleanup_user.append(body["accessToken"])
  
    @allure.title('Тест: Создание пользователя без обязательного поля')        
    @pytest.mark.parametrize("payload", [
        {"email": "user2222@yandex.ru", "name": "user2222"},
        {"password": "pass123", "name": "user2222"},
        {"email": "user2222@yandex.ru"}
    ])
    def test_create_user_incorrect_fields_fail(self, payload):
        user_api = UserApi()
        
        response = user_api.create_user(payload)
        body = response.json()

        assert response.status_code == 403
        assert body["message"] == ERROR_REQUIRED_FIELDS



