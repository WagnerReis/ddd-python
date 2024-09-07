from ddd_python.entity.order import Order
from ddd_python.entity.order_item import OrderItem
from ddd_python.service.order_service import OrderService


class TestOrderService:
    def test_should_get_total_of_all_orders(self):
        item1 = OrderItem("123", "456", "Item 1", 10, 1)
        item2 = OrderItem("123asd", "456213", "Item 2", 20, 1)

        order = Order("123", "456", [item1])
        order2 = Order("123123", "45645", [item2])

        total = OrderService.total([order, order2])

        assert total == 30

