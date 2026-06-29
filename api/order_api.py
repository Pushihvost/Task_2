from api.base_api import BaseApi
from data.endpoints import (
    CREATE_ORDER,
    GET_INGREDIENTS,
    GET_USER_ORDERS
)
import allure


class OrderApi(BaseApi):

    @allure.step("Создать заказ")
    def create_order(self, ingredients = None, token = None):
        return self.post(
            CREATE_ORDER, 
            payload = {"ingredients": ingredients} if ingredients else None,            
            headers={"Authorization": token} if token else None          
            )

    @allure.step("Получить ингредиенты")
    def get_ingredients(self):
        return self.get(GET_INGREDIENTS)

    @allure.step("Получить заказ")
    def get_order(self, token = None):
        return self.get(
            GET_USER_ORDERS,
            headers={"Authorization": token} if token else None 
            )


