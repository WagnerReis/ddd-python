from typing import List, Optional

from ddd_python.domain.entity.address import Address
from ddd_python.domain.entity.customer import Customer
from ddd_python.domain.repository.customer_repository_inteface import CustomerRepositoryInterface
from ddd_python.infrastructure.db.sqlalchemy.model.customer_model import CustomerModel
from ddd_python.main import address


class CustomerRepository(CustomerRepositoryInterface):
    def __init__(self, session):
        self._session = session

    def create(self, entity: Customer) -> None:
        customer = CustomerModel(
            customer_id=entity.get_id(),
            name=entity.get_name(),
            active=entity.is_active(),
            reward_points=entity.get_reward_points(),
            street=entity.address.street,
            number=entity.address.number,
            zipcode=entity.address.zip,
            city=entity.address.city
        )
        self._session.add(customer)
        self._session.commit()
        self._session.close()

    def update(self, entity: Customer) -> None:
        customer_model = self._session.query(CustomerModel).filter_by(customer_id=entity.get_id()).first()

        if customer_model:
            customer_model.name = entity.get_name()

            try:
                self._session.commit()
            except Exception as e:
                self._session.rollback()
                raise e
        else:
            raise ValueError(f"Customer with id {entity.get_id()} not found")

    def find(self, _id: str) -> Optional[Customer]:
        customer = self._session.query(CustomerModel).filter_by(customer_id=_id).first()
        if customer:
            return customer
        else:
            raise Exception("Customer not found")

    def find_all(self) -> List[Customer]:
        customer_models = self._session.query(CustomerModel).filter().all()

        def format_customer(customer_model):
            customer = Customer(
                customer_id=customer_model.customer_id,
                name=customer_model.name
            )
            address = Address(
                street=customer_model.street,
                number=customer_model.number,
                zip=customer_model.zipcode,
                city=customer_model.city
            )
            customer.change_address(address)
            customer.add_reward_points(customer_model.reward_points)
            return customer

        customers = list(map(format_customer, customer_models))
        return customers
