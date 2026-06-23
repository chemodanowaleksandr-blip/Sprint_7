import requests
import allure
from src.data import *


class scooterapi:

    @staticmethod
    @allure.step("Создание курьера (POST)")
    def create_courier(payload):
        return requests.post(CREATE_COURIER, json=payload)

    @staticmethod
    @allure.step("Логин курьера в системе (POST)")
    def login_courier(payload):
        return requests.post(LOGIN_COURIER, json=payload)

    @staticmethod
    @allure.step("Удаление курьера по ID (DELETE)")
    def delete_courier(courier_id):
        return requests.delete(f"{CREATE_COURIER}/{courier_id}")

    @staticmethod
    @allure.step("Создание заказа (POST)")
    def create_order(payload):
        return requests.post(ORDERS, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов (GET)")
    def get_orders_list():
        return requests.get(ORDERS)
