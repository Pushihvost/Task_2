from api.user_api import UserApi
from data.message_error import ERROR_INCORRECT_EMAIL_OR_PASSWORD
import allure

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
    def test_login_with_invalid_email_or_password(self, authorized_user):
        user = authorized_user['user']

        login_payload_invalid = [
            {
            'email': user['email'],
            'password': "no_correct_password"
            },
            {
            'email': "no_correct_email",
            'password': user['password']
            }
        ]

        for login_payload in login_payload_invalid:
            response = UserApi().login_user(login_payload)

            body = response.json()

            assert response.status_code == 401
            assert body["message"] == ERROR_INCORRECT_EMAIL_OR_PASSWORD



