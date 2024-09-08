from abc import ABC

from ddd_python.domain.entity.customer import Customer
from ddd_python.domain.repository.repository_interface import RepositoryInterface


class CustomerRepositoryInterface(RepositoryInterface[Customer], ABC):
    pass