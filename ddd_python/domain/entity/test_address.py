import pytest
from pydantic import ValidationError
from ddd_python.domain.entity.address import Address


class TestAddress:
    def test_should_create_valid_address(self):
        address = Address(street="Rua X", number=10, zip="12345-678", city="City X")

        assert address.street == "Rua X"
        assert address.number == 10
        assert address.zip == "12345-678"
        assert address.city == "City X"

    def test_should_raise_error_for_empty_street(self):
        with pytest.raises(ValidationError, match="Street cannot be empty"):
            Address(street="", number=10, zip="12345-678", city="City X")

    def test_should_raise_error_for_empty_zip(self):
        with pytest.raises(ValidationError, match="Zip cannot be empty"):
            Address(street="Rua X", number=10, zip="", city="City X")

    def test_should_raise_error_for_empty_city(self):
        with pytest.raises(ValidationError, match="City cannot be empty"):
            Address(street="Rua X", number=10, zip="12345-678", city="")

    def test_should_raise_error_for_invalid_number(self):
        with pytest.raises(ValidationError, match="Number must be greater than zero"):
            Address(street="Rua X", number=0, zip="12345-678", city="City X")

    def test_should_convert_address_to_string(self):
        address = Address(street="Rua X", number=10, zip="12345-678", city="City X")
        assert address.to_string() == "Rua X, 10, 12345-678, City X"
