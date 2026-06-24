import pytest
import allure
from src.courier_api import ScooterApi
from src.data import CourierData

@allure.epic("Управление курьерами")
@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_success_login(self, create_and_delete_courier):
        payload, _, courier_id = create_and_delete_courier
        
        response = ScooterApi.login_courier({"login": payload["login"], "password": payload["password"]})
        
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка при вводе неправильного логина или пароля")
    def test_login_with_wrong_credentials(self, create_and_delete_courier):
        payload, _, _ = create_and_delete_courier
        
        response = ScooterApi.login_courier({"login": payload["login"], "password": "wrong_password"})
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    def test_login_missing_field(self):
        payload = {"login": "some_login", "password": "some_password"}
        del payload[missing_field]
        
        try:
            response = ScooterApi.login_courier(payload)
            assert response.status_code == 400
            assert "Недостаточно данных для входа" in response.json()["message"]
        except Exception:
            pass
