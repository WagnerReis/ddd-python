import pytest

from ddd_python.entity.order import Order
from ddd_python.entity.order_item import OrderItem


class TestOrder:

    def test_should_throw_error_when_order_is_empty(self):
        with pytest.raises(ValueError, match="Id is required"):
            Order("", "123", [])

    def test_should_throw_error_when_customer_id_is_empty(self):
        with pytest.raises(ValueError, match="Customer id is required"):
            Order("123", "", [])

    def test_should_throw_error_when_items_are_empty(self):
        with pytest.raises(ValueError, match="Order must have at least one item"):
            Order("123", "123", [])

    def test_should_calculate_total(self):
        item1 = OrderItem("1", "123", "Item 1", 10, 1)
        item2 = OrderItem("2", "123", "Item 2", 20, 2)
        order = Order("123", "123", [item1, item2])
        assert order.total() == 50

    def test_should_throw_error_if_the_quantity_is_greater_lass_or_equal_zero(self):
        with pytest.raises(ValueError, match="Quantity must be greater than 0"):
            OrderItem("1", "123", "Item 1", 10, 0)