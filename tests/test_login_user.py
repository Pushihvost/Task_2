from api.user_api import UserApi
from data.message_error import ERROR_INCORRECT_EMAIL_OR_PASSWORD
import allure
import pytest
class TestLoginUser:

    @allure.title('Тест: Успешная авторизация существующего пользователя')
    def test_login_with_existing_user(self, authorized_user):

        user = authorized_user['user']

        login_payload = {
        'email': user['email'],
        'password': user['password']
    }

        response = UserApi().login_user(login_payload)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] == True

    @allure.title('Тест: Авторизация с неверным логином или паролем')
    @pytest.mark.parametrize(
        "field, value",
        [
            ("email", "wrong_email"),
            ("password", "wrong_password"),
        ]
    )
    def test_login_no_correct_login_or_password(self, authorized_user, field, value):
        user = authorized_user["user"]

        login_payload = {
            "email": user["email"],
            "password": user["password"]
        }

        login_payload[field] = value

        response = UserApi().login_user(login_payload)

        assert response.status_code == 401
        assert response.json()["message"] == ERROR_INCORRECT_EMAIL_OR_PASSWORD



