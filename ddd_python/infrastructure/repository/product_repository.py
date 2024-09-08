from typing import List, Optional

from ddd_python.domain.entity.product import Product
from ddd_python.domain.repository.product_repository_inteface import ProductRepositoryInterface
from ddd_python.infrastructure.db.sqlalchemy.model.product_model import ProductModel


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, session):
        self._session = session

    def create(self, entity: Product) -> None:
        product = ProductModel(
            product_id=entity.get_id(), name=entity.get_name(), price=entity.get_price()
        )
        self._session.add(product)
        self._session.commit()
        self._session.close()

    def update(self, entity: Product) -> None:
        product_model = self._session.query(ProductModel).filter_by(product_id=entity.get_id()).first()

        if product_model:
            product_model.name = entity.get_name()
            product_model.price = entity.get_price()

            try:
                self._session.commit()
            except Exception as e:
                self._session.rollback()
                raise e
        else:
            raise ValueError(f"Product with id {entity.get_id()} not found")

    def find(self, _id: str) -> Optional[Product]:
        return self._session.query(ProductModel).filter_by(product_id=_id).first()

    def find_all(self) -> List[Product]:
        return self._session.query(ProductModel).filter().all()
