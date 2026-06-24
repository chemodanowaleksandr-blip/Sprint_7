import random
import string

class Urls:
    BASE_URL = "https://praktikum-services.ru"
    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    ORDERS = f"{BASE_URL}/api/v1/orders"

class CourierData:
    @classmethod
    def generate_random_string(cls, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @classmethod
    def generate_new_couple_payload(cls):
        return {
            "login": cls.generate_random_string(),
            "password": cls.generate_random_string(),
            "firstName": cls.generate_random_string()
        }

class OrderData:
    BASE_ORDER_PAYLOAD = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Центральная, 1",
        "metroStation": 4,
        "phone": "+79991112233",
        "rentTime": 5,
        "deliveryDate": "2026-06-30",
        "comment": "Позвонить за час"
    }
