import pytest
import allure
from src.courier_api import ScooterApi
from src.data import CourierData

@allure.epic("Управление курьерами")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("Успешное создание курьера")
    @allure.description("Проверка, что нового курьера можно успешно создать с валидными данными")
    def test_success_create_courier(self):
        payload = CourierData.generate_new_courier_payload()
        response = ScooterApi.create_courier(payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        login_res = ScooterApi.login_courier({"login": payload["login"], "password": payload["password"]})
        if login_res.status_code == 200:
            ScooterApi.delete_courier(login_res.json()["id"])

    @allure.story("Создание дубликата курьера")
    @allure.description("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self):
        payload = CourierData.generate_new_courier_payload()
        
        res1 = ScooterApi.create_courier(payload)
        assert res1.status_code == 201
        
        res2 = ScooterApi.create_courier(payload)
        assert res2.status_code == 409
        assert "Этот логин уже используется" in res2.json()["message"]
        
        login_res = ScooterApi.login_courier({"login": payload["login"], "password": payload["password"]})
        if login_res.status_code == 200:
            ScooterApi.delete_courier(login_res.json()["id"])

    @allure.story("Валидация обязательных полей при создании")
    @allure.description("Проверка, что при отсутствии login или password возвращается 400 ошибка")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, missing_field):
        payload = CourierData.generate_new_courier_payload()
        del payload[missing_field]
        
        response = ScooterApi.create_courier(payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
