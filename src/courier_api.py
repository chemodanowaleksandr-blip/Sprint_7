import requests
import allure



class scooterapi:

    @staticmethod
    @allure.step("Создание курьера (POST)")
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, json=payload)

    @staticmethod
    @allure.step("Логин курьера в системе (POST)")
    def login_courier(payload):
        return requests.post(Urls.LOGIN_COURIER, json=payload)

    @staticmethod
    @allure.step("Удаление курьера по ID (DELETE)")
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")

    @staticmethod
    @allure.step("Создание заказа (POST)")
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов (GET)")
    def get_orders_list():
        return requests.get(Urls.ORDERS)
class urls:
    CREATE_COURIER = "https://praktikum-services.ru"
    LOGIN_COURIER = "https://praktikum-services.ru/login"
    ORDERS = "https://praktikum-services.ru"


