from typing import List

from ddd_python.entity.order_item import OrderItem


class Order:
    def __init__(self, order_id: str, curtomer_id: str, items: List[OrderItem]):
        self._id = order_id
        self._customer_id = curtomer_id
        self._items = items
