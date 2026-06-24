import pytest
import allure
from src.courier_api import ScooterApi
from src.data import CourierData

@allure.epic("Управление курьерами")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_success_create_courier(self):
        payload = CourierData.generate_new_couple_payload()
        response = ScooterApi.create_courier(payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        login_res = ScooterApi.login_courier({"login": payload["login"], "password": payload["password"]})
        if login_res.status_code == 200:
            ScooterApi.delete_courier(login_res.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self, create_and_delete_courier):
        existing_payload, _, _ = create_and_delete_courier
        
        response = ScooterApi.create_courier(existing_payload)
        
        assert response.status_code == 409
        assert "Этот логин уже занят" in response.json()["message"]

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    @allure.title("Ошибка создания курьера при отсутствии обязательного поля")
    def test_create_courier_missing_field(self, missing_field):
        payload = CourierData.generate_new_couple_payload()
        del payload[missing_field]
        
        response = ScooterApi.create_courier(payload)
        
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json()["message"]
