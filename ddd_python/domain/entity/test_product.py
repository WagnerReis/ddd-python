import pytest

from ddd_python.domain.entity.product import Product


class TestProduct:
    def test_should_throw_error_when_id_is_empty(self):
        with pytest.raises(ValueError, match="Id is required"):
            Product("", "Product 1",10)

    def test_should_throw_error_when_name_is_empty(self):
        with pytest.raises(ValueError, match="Name is required"):
            Product("1", "", 10)

    def test_should_throw_error_when_price_is_less_than_zero(self):
        with pytest.raises(ValueError, match="Price must be greater than zero"):
            Product("1", "Product 1", -1)

    def test_should_change_name(self):
        product = Product("1", "Product 1", 10)
        product.change_name("Product 2")
        assert product.get_name() == "Product 2"

    def test_should_change_price(self):
        product = Product("1", "Product 1", 10)
        product.change_price(20)
        assert product.get_price() == 20