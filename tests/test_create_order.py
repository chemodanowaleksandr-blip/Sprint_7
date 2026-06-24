import pytest
import allure
from src.courier_api import scooterapi
from src.data import OrderData

@allure.epic("Управление заказами")
@allure.feature("Создание и получение заказов")
class TestOrders:

    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с различными вариациями цветов")
    def test_create_order_with_different_colors(self, colors):
        payload = OrderData.BASE_ORDER_PAYLOAD.copy()
        payload["color"] = colors
        
        response = scooterapi.create_order(payload)
        
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = scooterapi.get_orders_list()
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
