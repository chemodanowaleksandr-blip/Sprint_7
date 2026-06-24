import pytest
from src.courier_api import ScooterApi
from src.data import CourierData

@pytest.fixture
def create_and_delete_courier():
    payload = CourierData.generate_new_couple_payload()
    response = ScooterApi.create_courier(payload)
    
    courier_id = None
    login_response = ScooterApi.login_courier({"login": payload["login"], "password": payload["password"]})
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        
    yield payload, response, courier_id

    if courier_id:
        ScooterApi.delete_courier(courier_id)
