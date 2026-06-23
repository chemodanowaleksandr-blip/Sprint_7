import requests
import allure


class scooterapi:
    # Прописываем рабочий стенд Практикума напрямую через IP, минуя сломанный DNS!
    CREATE_COURIER = "https://130.193.53"
    LOGIN_COURIER = "https://130.193.53/login"
    ORDERS = "https://130.193.53"

    @staticmethod
    @allure.step("Создание курьера (POST)")
    def create_courier(payload):
        # Отключаем строгую проверку SSL-сертификата (verify=False), так как идем по IP
        return requests.post(scooterapi.CREATE_COURIER, json=payload, verify=False)

    @staticmethod
    @allure.step("Логин курьера в системе (POST)")
    def login_courier(payload):
        return requests.post(scooterapi.LOGIN_COURIER, json=payload, verify=False)

    @staticmethod
    @allure.step("Удаление курьера по ID (DELETE)")
    def delete_courier(courier_id):
        return requests.delete(f"{scooterapi.CREATE_COURIER}/{courier_id}", verify=False)

    @staticmethod
    @allure.step("Создание заказа (POST)")
    def create_order(payload):
        return requests.post(scooterapi.ORDERS, json=payload, verify=False)

    @staticmethod
    @allure.step("Получение списка заказов (GET)")
    def get_orders_list():
        return requests.get(scooterapi.ORDERS, verify=False)
