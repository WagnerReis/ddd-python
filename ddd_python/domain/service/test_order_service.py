from ddd_python.domain.entity.order import Order
from ddd_python.domain.entity.order_item import OrderItem
from ddd_python.domain.entity.customer import Customer
from ddd_python.domain.service.order_service import OrderService


class TestOrderService:
    def test_should_place_an_order(self):
        customer = Customer("c1", "customer 1")
        item1 = OrderItem("123", "456", "Item 1", 10, 1)

        order = OrderService.place_orders(customer, [item1])

        assert customer.get_reward_points() == 5
        assert order.total() == 10

    def test_should_throw_an_error_when_order_items_is_empty(self):
        customer = Customer("c1", "customer 1")

        try:
            OrderService.place_orders(customer, [])
        except Exception as e:
            assert str(e) == "At least one item is required"

    def test_should_get_total_of_all_orders(self):
        item1 = OrderItem("123", "456", "Item 1", 10, 1)
        item2 = OrderItem("123asd", "456213", "Item 2", 20, 1)

        order = Order("123", "456", [item1])
        order2 = Order("123123", "45645", [item2])

        total = OrderService.total([order, order2])

        assert total == 30

