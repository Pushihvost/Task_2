from api.order_api import OrderApi
from data.message_error import ERROR_NO_IDS
import allure


class TestCreateOrder:

    @allure.title('Тест: Успешное создание заказа с ингридиентами авторизированным пользователем')
    def test_create_order_authorized_user_with_ingredient(self, authorized_user):

        token = authorized_user['token']

        ingredients_response = OrderApi().get_ingredients()
        body_ing = ingredients_response.json()["data"]
        ingredients = [
                        body_ing[0]["_id"],
                        body_ing[1]["_id"]
                    ]

        response = OrderApi().create_order(ingredients, token)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body
        assert "owner" in body["order"]

    @allure.title('Тест: Успешное создание заказа с ингридиентами неавторизированным пользователем')
    def test_create_order_unauthorized_user_with_ingredient(self):


        ingredients_response = OrderApi().get_ingredients()
        body_ing = ingredients_response.json()["data"]
        ingredients = [
                        body_ing[0]["_id"],
                        body_ing[1]["_id"]
                    ]

        response = OrderApi().create_order(ingredients)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body
   
    @allure.title('Тест: Неуспешное создание заказа без ингридиентов неавторизированным пользователем')
    def test_create_order_unauthorized_user_no_ingredient(self):

        ingredients = []

        response = OrderApi().create_order(ingredients)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == ERROR_NO_IDS

    @allure.title('Тест: Неуспешное создание заказа без ингридиентов авторизированным пользователем')
    def test_create_order_authorized_user_no_ingredient(self, authorized_user):

        token = authorized_user['token']

        ingredients = []                    

        response = OrderApi().create_order(ingredients, token)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == ERROR_NO_IDS

    @allure.title('Тест: Неуспешное создание заказа с неверным хэшем ингридиента')
    def test_create_order_authorized_incorrect_hash_ids(self, authorized_user):

        token = authorized_user['token']

        ingredients = ["123"]                    

        response = OrderApi().create_order(ingredients, token)

        assert response.status_code == 500

