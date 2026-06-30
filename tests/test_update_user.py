from api.user_api import UserApi
from data.message_error import ERROR_UNAUTHORIZED
import pytest
import allure

class TestUpdateUser:

    @allure.title('Тест: Успешное изменение данных пользователя авторизованным пользователем')
    def test_authorized_user_change_profile_data(self, authorized_user):
        user = authorized_user['user']
        token = authorized_user['token']

        payload_for_patch = {
        'email': user['email']+"2",
        'name': user['name']+"2",
        'password': '1qaz2wsx'
    }

        response = UserApi().update_user(payload_for_patch, token)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] == True
        assert body["user"]["email"] == payload_for_patch["email"]
        assert body["user"]["name"] == payload_for_patch["name"]
 
    @allure.title('Тест: Неспешное изменение данных пользователя неавторизованным пользователем')
    @pytest.mark.parametrize("token", [None, "invalid_token"])
    def test_update_user_without_authorization(self, token):
        payload_for_patch = {
        'email': 'test2222@yandex.ru',
        'name': 'test2222',
        'password': '1qaz2wsx'
    }
        response = UserApi().update_user(payload_for_patch, token)
        body = response.json()

        assert response.status_code == 401
        assert body["success"] == False
        assert body["message"] == ERROR_UNAUTHORIZED