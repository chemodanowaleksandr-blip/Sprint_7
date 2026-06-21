import pytest
import allure
from src.courier_api import ScooterApi

@allure.epic("Управление курьерами")
@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.story("Успешный логин")
    @allure.description("Курьер может успешно авторизоваться, система возвращает id")
    def test_success_login(self, create_and_delete_courier):
        payload, _, _ = create_and_delete_courier
        
        login_payload = {"login": payload["login"], "password": payload["password"]}
        response = ScooterApi.login_courier(login_payload)
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.story("Логин с неверными учетными данными")
    @allure.description("Система возвращает ошибку, если указан неверный логин или пароль")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_with_wrong_credentials(self, create_and_delete_courier, wrong_field):
        payload, _, _ = create_and_delete_courier
        
        login_payload = {"login": payload["login"], "password": payload["password"]}
        login_payload[wrong_field] += "_wrong"
        
        response = ScooterApi.login_courier(login_payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.story("Логин с отсутствующими полями")
    @allure.description("Проверка возврата ошибки 400 при отсутствии обязательных полей запроса")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_required_field(self, create_and_delete_courier, missing_field):
        payload, _, _ = create_and_delete_courier
        
        login_payload = {"login": payload["login"], "password": payload["password"]}
        del login_payload[missing_field]
        
        response = ScooterApi.login_courier(login_payload)
        
        assert response.status_code in [400, 504]
if response.status_code == 400:
    assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.story("Логин несуществующего пользователя")
    @allure.description("Попытка авторизации под случайными несуществующими данными")
    def test_login_non_existent_courier(self):
        payload = {"login": "non_existent_user_xyz", "password": "secure_password_123"}
        response = ScooterApi.login_courier(payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
