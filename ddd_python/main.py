from ddd_python.domain.entity.address import Address
from ddd_python.domain.entity.customer import Customer
from ddd_python.domain.entity.order import Order
from ddd_python.domain.entity.order_item import OrderItem

customer = Customer("123", "Wagner")
address = Address(street="Rua dois", number=2, zip="12345-678", city="São Paulo")
customer.address = address
customer.activate()

item1 = OrderItem("1", "123", "item 1", 10, 1)
item2 = OrderItem("2", "123", "item 2", 15, 2)

order = Order("1", customer.get_id(), [item1, item2])
print(order.total())

