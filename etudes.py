
from app.models import *

products_list = [
        {"id": 1, "name": "Manzana", "unit_price": 1.2, "quantity": 1, "subtotal": 1.2},
        {"id": 2, "name": "Plátano", "unit_price": 0.8, "quantity": 0, "subtotal": 0},
        {"id": 3, "name": "Naranja", "unit_price": 1.2, "quantity": 2, "subtotal": 2.4}
    ]
    
ticket = Ticket(products_list)
        
ticket.add_product(2, 2)
assert ticket.products_list[1]["quantity"] == 2
assert ticket.products_list[1]["subtotal"] == 1.6

ticket.add_product(3, 3)
assert ticket.products_list[2]["quantity"] == 5
assert ticket.products_list[2]["subtotal"] == 6

ticket.add_product(2, 3)
assert ticket.products_list[1]["quantity"] == 5
assert ticket.products_list[1]["subtotal"] == 4

ticket.add_product(1, 1)
assert ticket.products_list[0]["quantity"] == 2
assert ticket.products_list[0]["subtotal"] == 2.4

print(products_list)
print(ticket.total_ticket())