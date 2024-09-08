from typing import List, Optional

from ddd_python.domain.entity.customer import Customer
from ddd_python.domain.repository.customer_repository_inteface import CustomerRepositoryInterface
from ddd_python.infrastructure.db.mappers.customer_mapper import CustomerMapper
from ddd_python.infrastructure.db.sqlalchemy.model.customer_model import CustomerModel


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
        return [CustomerMapper.to_domain(customer_model) for customer_model in customer_models]
