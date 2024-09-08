from unittest.mock import patch, MagicMock
import pytest
from uuid import uuid4
from sqlalchemy.exc import SQLAlchemyError

from ddd_python.domain.entity.address import Address
from ddd_python.domain.entity.customer import Customer
from ddd_python.infrastructure.db.sqlalchemy.model.customer_model import CustomerModel
from ddd_python.infrastructure.db.sqlalchemy.config import db_session
from ddd_python.infrastructure.repository.customer_repository import CustomerRepository


class CreateCustomerTestFactory:
    """
    Factory class to create a Customer object for testing purposes.
    """

    @staticmethod
    def create_customer(customer_id: str):
        customer = Customer(customer_id, "customer 1")
        address = Address(street="street 1", city="city 1", zip="state 1", number=12345)
        customer.change_address(address)

        return customer, address


class TestCustomerRepository:
    def test_should_create_a_customer(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = "123"
        customer, address = CreateCustomerTestFactory().create_customer(customer_id)
        customer_repository.create(customer)

        customer_model = db_session.query(CustomerModel).filter_by(customer_id=customer_id).first()
        assert customer_model is not None
        assert customer_model.name == customer.get_name()
        assert customer_model.active == customer.is_active()
        assert customer_model.reward_points == customer.get_reward_points()
        assert customer_model.street == address.street
        assert customer_model.number == address.number
        assert customer_model.zipcode == address.zip
        assert customer_model.city == address.city

    def test_should_update_a_customer(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = "123"
        customer, address = CreateCustomerTestFactory().create_customer(customer_id)
        customer_repository.create(customer)

        customer.change_name("customer 2")
        customer_repository.update(customer)

        customer_model = db_session.query(CustomerModel).filter_by(customer_id=customer_id).first()
        assert customer_model is not None
        assert customer_model.customer_id == customer_id
        assert customer_model.name == "customer 2"

    def test_should_throw_an_exception_when_try_update_a_customer_that_not_exists(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = "1231323123213"
        customer = Customer(customer_id, "customer 1")

        with pytest.raises(ValueError, match=f"Customer with id {customer_id} not found"):
            customer_repository.update(customer)

    def test_commit_exception_triggers_rollback(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = "123"
        customer, address = CreateCustomerTestFactory().create_customer(customer_id)
        customer_repository.create(customer)

        db_session.rollback = MagicMock()

        with patch.object(db_session, 'commit', side_effect=SQLAlchemyError("Commit failed")):
            with pytest.raises(SQLAlchemyError, match="Commit failed"):
                customer_repository.update(customer)

        db_session.rollback.assert_called_once()

    def test_should_not_found_a_customer_by_id(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = str(uuid4())
        with pytest.raises(Exception, match=f"Customer not found"):
            customer_repository.find(customer_id)

    def test_should_find_a_customer_by_id(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = "123"
        customer, address = CreateCustomerTestFactory().create_customer(customer_id)
        customer_repository.create(customer)

        customer_found = customer_repository.find(customer_id)
        assert customer_found is not None
        assert customer_found.name == customer.get_name()
        assert customer_found.active == customer.is_active()
        assert customer_found.reward_points == customer.get_reward_points()
        assert customer_found.street == address.street
        assert customer_found.number == address.number
        assert customer_found.zipcode == address.zip
        assert customer_found.city == address.city

    def test_should_find_all_customers(self, db_session):
        customer_repository = CustomerRepository(db_session)
        customer_id = "123"
        customer, address = CreateCustomerTestFactory().create_customer(customer_id)
        customer_repository.create(customer)

        customers = customer_repository.find_all()
        assert len(customers) == 1
        assert customers is not None
        assert customers[0].get_name() == customer.get_name()
        assert customers[0].is_active() == customer.is_active()
        assert customers[0].get_reward_points() == customer.get_reward_points()
        assert customers[0].address.street == address.street
        assert customers[0].address.number == address.number
        assert customers[0].address.zip == address.zip
        assert customers[0].address.city == address.city
