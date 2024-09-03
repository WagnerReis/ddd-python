from .address import Address


class Customer:
    def __init__(self, customer_id: str, name: str, address: Address):
        self._id = customer_id
        self._name = name
        self._address = address
        self._active: bool = True
        self.validate()

    def validate(self):
        if not self._id:
            raise ValueError("Id is required")

        if not self._name:
            raise ValueError("Name is required")

    def change_name(self, name: str):
        self._name = name
        self.validate()

    def activate(self):
        if not self._address:
            raise ValueError("Address is mandatory to activate a customer")
        self._active = True

    def deactivate(self):
        self._active = False

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address
