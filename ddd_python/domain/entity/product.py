class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self._product_id = product_id
        self._name = name
        self._price = price
        self.validate()

    def get_id(self):
        return self._product_id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def change_name(self, name: str):
        self._name = name
        self.validate()

    def change_price(self, price: float):
        self._price = price
        self.validate()

    def validate(self):
        if not self._product_id:
            raise ValueError("Id is required")
        if not self._name:
            raise ValueError("Name is required")
        if self._price < 0:
            raise ValueError("Price must be greater than zero")
