from ddd_python.domain.entity.address import Address
from ddd_python.domain.entity.customer import Customer
from ddd_python.infrastructure.db.sqlalchemy.model.customer_model import CustomerModel


class CustomerMapper:
    @staticmethod
    def to_domain(customer_model: CustomerModel) -> Customer:
        """
        Convert a CustomerModel instance to a Customer domain object.

        :param customer_model: The CustomerModel instance to convert.
        :return: The corresponding Customer domain object.
        """
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