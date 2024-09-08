from abc import ABC

from ddd_python.domain.entity.product import Product
from ddd_python.domain.repository.repository_interface import RepositoryInterface


class ProductRepositoryInterface(RepositoryInterface[Product], ABC):
    pass