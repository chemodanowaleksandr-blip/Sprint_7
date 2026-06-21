import requests
from src.data import Urls

class ScooterApi:
    @staticmethod
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, json=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(Urls.LOGIN_COURIER, json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")

    @staticmethod
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload)

    @staticmethod
    def get_orders_list():
        return requests.get(Urls.ORDERS)
