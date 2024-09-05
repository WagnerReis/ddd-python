import pytest

from ddd_python.entity.address import Address
from ddd_python.entity.customer import Customer


class TestCustomer:
    def test_should_throw_error_when_name_is_empty(self):
        with pytest.raises(ValueError, match="Id is required"):
            Customer("", "John Doe")

    def test_should_throw_error_when_id_is_empty(self):
        with pytest.raises(ValueError, match="Name is required"):
            Customer("123", "")

    def test_should_change_name(self):
        customer = Customer("123", "John")
        customer.change_name("John Doe")
        assert customer.get_name() == "John Doe"

    def test_should_return_customer_id(self):
        customer = Customer("123", "John")
        assert customer.get_id() == "123"

    def test_should_activate_customer(self):
        customer = Customer("123", "John")
        address = Address(street="Rua X", number=1, zip="121231-123", city="City X")
        customer.address = address
        customer.activate()

        assert customer.is_active()

    def test_should_return_customer_address(self):
        customer = Customer("123", "John")
        address = Address(street="Rua X", number=1, zip="121231-123", city="City X")
        customer.address = address

        assert isinstance(customer.address, Address)

    def test_should_deactivate_customer(self):
        customer = Customer("123", "John")
        customer.deactivate()

        assert not customer.is_active(), "Customer should be deactivated"

    def test_should_throw_error_when_address_is_undefined_when_activate(self):
        with pytest.raises(ValueError, match="Address is mandatory to activate a customer"):
            customer = Customer("123", "John")
            customer.activate()
