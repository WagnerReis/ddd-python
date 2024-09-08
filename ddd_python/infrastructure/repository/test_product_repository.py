from unittest.mock import patch, MagicMock
import pytest
from uuid import uuid4
from sqlalchemy.exc import SQLAlchemyError

from ddd_python.domain.entity.product import Product
from ddd_python.infrastructure.db.sqlalchemy.model.product_model import ProductModel
from ddd_python.infrastructure.db.sqlalchemy.config import db_session
from ddd_python.infrastructure.repository.product_repository import ProductRepository


class TestProductRepository:
    def test_should_create_a_product(self, db_session):
        product_repository = ProductRepository(db_session)
        product = Product("123", "product 1", 10)

        product_repository.create(product)

        product_model = db_session.query(ProductModel).filter_by(product_id="123").first()
        assert product_model is not None
        assert product_model.name == "product 1"
        assert product_model.price == 10.0
        assert product_model.product_id == "123"

    def test_should_update_a_product(self, db_session):
        product_repository = ProductRepository(db_session)
        product_id = "123456"
        product = Product(product_id, "product 1", 10)
        product_repository.create(product)

        product.change_name("product 2")
        product.change_price(20.0)
        product_repository.update(product)

        product_model = db_session.query(ProductModel).filter_by(product_id=product_id).first()
        assert product_model is not None
        assert product_model.product_id == product_id
        assert product_model.name == "product 2"
        assert product_model.price == 20.0

    def test_should_throw_an_exception_when_try_update_a_product_that_not_exists(self, db_session):
        product_repository = ProductRepository(db_session)
        product_id = "1231323123213"
        product = Product(product_id, "product 1", 10)

        with pytest.raises(ValueError, match=f"Product with id {product_id} not found"):
            product_repository.update(product)

    def test_commit_exception_triggers_rollback(self, db_session):
        product_repository = ProductRepository(db_session)
        product = Product("123", "Test Product", 99.99)
        product_repository.create(product)

        db_session.rollback = MagicMock()

        with patch.object(db_session, 'commit', side_effect=SQLAlchemyError("Commit failed")):
            with pytest.raises(SQLAlchemyError, match="Commit failed"):
                product_repository.update(product)

        db_session.rollback.assert_called_once()

    def test_should_not_found_a_product_by_id(self, db_session):
        product_repository = ProductRepository(db_session)
        product_id = str(uuid4())
        product_found = product_repository.find(product_id)
        assert product_found is None

    def test_should_find_a_product_by_id(self, db_session):
        product_repository = ProductRepository(db_session)
        product_id = "12345"
        product = Product(product_id, "product 1", 10)
        product_repository.create(product)

        product_found = product_repository.find(product_id)
        assert product_found is not None
        assert product_found.product_id == product.get_id()
        assert product_found.name == product.get_name()
        assert product_found.price == product.get_price()

    def test_should_find_all_products(self, db_session):
        product_repository = ProductRepository(db_session)
        product_id = str(uuid4())
        product = Product(product_id, "product 1", 10)
        product_repository.create(product)

        products = product_repository.find_all()
        assert len(products) == 1
        assert products[0].product_id == product.get_id()
        assert products[0].name == product.get_name()
        assert products[0].price == product.get_price()
