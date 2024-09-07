class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.validate()

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def change_name(self, name: str):
        self.name = name
        self.validate()

    def change_price(self, price: float):
        self.price = price
        self.validate()

    def validate(self):
        if not self.product_id:
            raise ValueError("Id is required")
        if not self.name:
            raise ValueError("Name is required")
        if self.price < 0:
            raise ValueError("Price must be greater than zero")
