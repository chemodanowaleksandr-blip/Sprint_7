import pytest
import src.courier_api
from src.data import CourierData

@pytest.fixture
def create_and_delete_courier():
    payload = CourierData.generate_new_couple_payload()
    
    # Ищем класс автоматически, независимо от регистра первой буквы
    api_class = getattr(src.courier_api, "ScooterApi", getattr(src.courier_api, "scooterapi", None))
    
    response = api_class.create_courier(payload)
    courier_id = None
    login_response = api_class.login_courier({"login": payload["login"], "password": payload["password"]})
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        
    yield payload, response, courier_id

    if courier_id:
        api_class.delete_courier(courier_id)
