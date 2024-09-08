class OrderItem:
    def __init__(self, order_item_id: str, product_id: str, name: str, price: float, quantity: int):
        self._id = order_item_id
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity
        self.validate()

    def get_order_item_total(self) -> float:
        return self._price * self._quantity

    def validate(self):
        if self._quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
