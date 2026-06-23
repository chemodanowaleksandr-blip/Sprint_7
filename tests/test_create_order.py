import pytest
import allure
from src.courier_api import scooterapi
from src.data import OrderData


@allure.epic("Управление заказами")
class TestOrders:

    @allure.feature("Создание заказа")
    @allure.story("Параметризованный выбор цветов")
    @allure.description("Проверка создания заказа с разными конфигурациями цветов: BLACK, GREY, оба цвета или пустой")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        payload = OrderData.BASE_ORDER_PAYLOAD.copy()
        payload["color"] = color

        response = scooterapi.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)

    @allure.feature("Получение списка заказов")
    @allure.story("Просмотр заказов в системе")
    @allure.description("Проверка, что запрос на получение списка возвращает массив с ключом 'orders'")
    def test_get_orders_list_returns_orders(self):
        response = scooterapi.get_orders_list()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
        assert len(response.json()["orders"]) >= 0
