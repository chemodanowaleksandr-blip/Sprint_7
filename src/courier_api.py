import requests
import allure


class scooterapi:
    # Объявляем урлы прямо внутри класса – теперь они гарантированно доступны везде!
    CREATE_COURIER = "https://praktikum-services.ru"
    LOGIN_COURIER = "https://praktikum-services.ru/login"
    ORDERS = "https://praktikum-services.ru"

    @staticmethod
    @allure.step("Создание курьера (POST)")
    def create_courier(payload):
        return requests.post(scooterapi.CREATE_COURIER, json=payload)

    @staticmethod
    @allure.step("Логин курьера в системе (POST)")
    def login_courier(payload):
        return requests.post(scooterapi.LOGIN_COURIER, json=payload)

    @staticmethod
    @allure.step("Удаление курьера по ID (DELETE)")
    def delete_courier(courier_id):
        return requests.delete(f"{scooterapi.CREATE_COURIER}/{courier_id}")

    @staticmethod
    @allure.step("Создание заказа (POST)")
    def create_order(payload):
        return requests.post(scooterapi.ORDERS, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов (GET)")
    def get_orders_list():
        return requests.get(scooterapi.ORDERS)
