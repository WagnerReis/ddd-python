from ddd_python.domain.entity import Product
from ddd_python.domain.service.product_service import ProductService


class TestProductService:
    def test_should_change_price_of_all_products(self):
        product1 = Product("123", "Product 1", 10, 1)
        product2 = Product("456", "Product 2", 20, 2)
        products = [product1, product2]

        ProductService.increase_price(products, 100)

        assert product1.get_price() == 20
        assert product2.get_price() == 40