from typing import List
from functools import reduce

from ddd_python.entity.order import Order


class OrderService:
    @staticmethod
    def total(orders: List[Order]) -> float:
        return reduce(lambda a, b: a + b.total(), orders, 0)