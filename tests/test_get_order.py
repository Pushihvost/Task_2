from api.order_api import OrderApi
from data.message_error import ERROR_UNAUTHORIZED
import allure


class TestGetOrder:

    @allure.title('Тест: Успешное получение заказов авторизированным пользователем')
    def test_get_order_authorized_user(self, authorized_user):

        token = authorized_user['token']

        response = OrderApi().get_order(token)

        body = response.json()

        assert response.status_code == 200
        assert "orders" in body

    @allure.title('Тест: Неуспешное получение заказов авторизированным пользователем')
    def test_get_order_unauthorized_user(self):

        response = OrderApi().get_order()

        body = response.json()

        assert response.status_code == 401
        assert body["message"] == ERROR_UNAUTHORIZED


