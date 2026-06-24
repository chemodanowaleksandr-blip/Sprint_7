import requests
import allure
from src.data import Urls

class ScooterApi:
    @staticmethod
    @allure.step("Создание курьера (POST /api/v1/courier)")
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, json=payload)

    @staticmethod
    @allure.step("Логин курьера в системе (POST /api/v1/courier/login)")
    def login_courier(payload):
        # Добавляем timeout=5, чтобы предотвратить бесконечное зависание сервера Практикума
        return requests.post(Urls.LOGIN_COURIER, json=payload, timeout=5)

    @staticmethod
    @allure.step("Удаление курьера по ID (DELETE /api/v1/courier/:id)")
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")

    @staticmethod
    @allure.step("Создание заказа (POST /api/v1/orders)")
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов (GET /api/v1/orders)")
    def get_orders_list():
        return requests.get(Urls.ORDERS)
