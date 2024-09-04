class OrderItem:
    def __init__(self, order_item_id: str, name: str, price: int):
        self._id = order_item_id
        self._name = name
        self._price = price
