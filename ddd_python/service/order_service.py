from typing import List
from functools import reduce
import uuid

from ddd_python.entity.customer import Customer
from ddd_python.entity.order import Order
from ddd_python.entity.order_item import OrderItem


class OrderService:
    @staticmethod
    def place_orders(customer: Customer, items: List[OrderItem]) -> Order:
        if len(items) == 0:
            raise ValueError("At least one item is required")

        order = Order(str(uuid.uuid4()), customer.get_id(), items)
        customer.add_reward_points(order.total() / 2)
        return order

    @staticmethod
    def total(orders: List[Order]) -> float:
        return reduce(lambda a, b: a + b.total(), orders, 0)