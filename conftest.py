import pytest
from src.courier_api import scooterapi
from src.data import CourierData


@pytest.fixture
def create_and_delete_courier():
    """
    Создает курьера перед тестом.
    После завершения теста автоматически удаляет его по ID (если логин успешный).
    """
    payload = CourierData.generate_new_courier_payload()
    response = scooterapi.create_courier(payload)

    courier_id = None
    login_response = scooterapi.login_courier({"login": payload["login"], "password": payload["password"]})
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")

    yield payload, response, courier_id

    if courier_id:
        scooterapi.delete_courier(courier_id)
