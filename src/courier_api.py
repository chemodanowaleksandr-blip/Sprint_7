import requests
import allure
from src.data import urls


class ScooterApi:

    @allure.step("Создание курьера (POST)")
    @staticmethod
    def create_courier(payload):
        return requests.post(urls.CREATE_COURIER, json=payload)

    @allure.step("Логин курьера в системе (POST)")
    @staticmethod
    def login_courier(payload):
        return requests.post(urls.LOGIN_COURIER, json=payload)

    @allure.step("Удаление курьера по ID (DELETE)")
    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{urls.CREATE_COURIER}/{courier_id}")

    @allure.step("Создание заказа (POST)")
    @staticmethod
    def create_order(payload):
        return requests.post(urls.ORDERS, json=payload)

    @allure.step("Получение списка заказов (GET)")
    @staticmethod
    def get_orders_list():
        return requests.get(urls.ORDERS)
