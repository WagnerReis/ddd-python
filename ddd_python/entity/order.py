from typing import List
import functools

from ddd_python.entity.order_item import OrderItem


class Order:
    def __init__(self, order_id: str, customer_id: str, items: List[OrderItem]):
        self._id = order_id
        self._customer_id = customer_id
        self._items = items
        self.validate()

    def validate(self):
        if not self._id:
            raise ValueError("Id is required")

        if not self._customer_id:
            raise ValueError("Customer id is required")

        if len(self._items) == 0:
            raise ValueError("Order must have at least one item")

    def total(self):
        return functools.reduce(lambda a, b: a + b.get_order_item_total(), self._items, 0)
