import pytest
import allure
import src.courier_api
from src.data import CourierData

@allure.epic("Управление курьерами")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @property
    def api(self):
        return getattr(src.courier_api, "ScooterApi", getattr(src.courier_api, "scooterapi", None))

    @allure.title("Успешное создание курьера")
    def test_success_create_courier(self):
        payload = CourierData.generate_new_couple_payload()
        response = self.api.create_courier(payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        login_res = self.api.login_courier({"login": payload["login"], "password": payload["password"]})
        if login_res.status_code == 200:
            self.api.delete_courier(login_res.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self, create_and_delete_courier):
        existing_payload, _, _ = create_and_delete_courier
        
        response = self.api.create_courier(existing_payload)
        
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

    # Исключили firstName, так как это необязательное поле в API Самоката
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Ошибка создания курьера при отсутствии обязательного поля")
    def test_create_courier_missing_field(self, missing_field):
        payload = CourierData.generate_new_couple_payload()
        del payload[missing_field]
        
        response = self.api.create_courier(payload)
        
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json()["message"]
