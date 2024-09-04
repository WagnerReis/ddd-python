from ddd_python.entity.order import Order
from ddd_python.entity.customer import Customer
from ddd_python.entity.address import Address
from ddd_python.entity.order_item import OrderItem


customer = Customer("123", "Wagner")
address = Address(street="Rua dois", number=2, zip="12345-678", city="São Paulo")
customer.address = address
customer.activate()

item1 = OrderItem("1", "item 1", 10)
item2 = OrderItem("2", "item 2", 15)

order = Order("1", customer.get_id(), [item1, item2])

