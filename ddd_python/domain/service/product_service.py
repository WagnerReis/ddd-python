from typing import List

from ddd_python.domain.entity import Product


class ProductService:
    @staticmethod
    def increase_price(products: List[Product], percentage: float) -> List[Product]:
        return [product.change_price((product.get_price() * percentage) / 100 + product.get_price()) or product for
                product in products]
