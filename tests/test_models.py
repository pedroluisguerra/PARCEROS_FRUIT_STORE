from app.models import *

def test_create_product():
    product = Product(3,"Naranja",0.70)

    assert product.id == 3
    assert product.name == "Naranja"
    assert product.unit_price == 0.70

    product = Product(2,"Plátano",0.30)

    assert product.id == 2
    assert product.name == "Plátano"
    assert product.unit_price == 0.30 

def test_dao_get_all_products():
    dao = DAO_Product(r"data\products.db")
    product_list = dao.get_all_products()

    assert len(product_list) == 10
    assert product_list[6]["name"] == "Tomate"
    assert product_list[6]["unit_price"] == 0.80
    assert product_list[1]["name"] == "Plátano"
    assert product_list[1]["unit_price"] == 0.30
    
def test_dao_get_product_by_id():
    dao = DAO_Product(r"data\products.db")
    product1 = dao.get_product_by_id(7)
    product2 = dao.get_product_by_id(3)

    assert  product1["name"] == "Tomate"
    assert  product1["unit_price"] == 0.80
    assert  product2["name"] == "Naranja"
    assert  product2["unit_price"] == 0.70

def test_add_product_ticket():
    ticket = Ticket()
    
    products_list = [
        {"id": 1, "name": "Manzana", "quantity": 10, "unit_price": 1.2},
        {"id": 2, "name": "Plátano", "quantity": 5, "unit_price": 0.8},
        {"id": 3, "name": "Naranja", "quantity": 2, "unit_price": 1.2}
    ]

        
    ticket.add_product(products_list[1], products_list[1]["quantity"])
    assert ticket.products[2]["quantity"] == 5
    assert ticket.products[2]["subtotal"] == 4

    ticket.add_product(products_list[2], products_list[2]["quantity"])
    assert ticket.products[3]["quantity"] == 2
    assert ticket.products[3]["subtotal"] == 2.40

def test_update_quantities():
    ticket = Ticket()
    products_list = [
        {"id": 1, "name": "Manzana", "quantity": 10, "unit_price": 1.2},
        {"id": 2, "name": "Plátano", "quantity": 5, "unit_price": 0.8},
        {"id": 1, "name": "Manzana", "quantity": 3, "unit_price": 1.2}
    ]
    
    ticket.update_quantities(products_list)
    
    assert ticket.products[1]["quantity"] == 13
    assert ticket.products[2]["quantity"] == 5

def test_total_product_list():
    ticket = Ticket()
    
    products_list = [
        {"id": 1, "name": "Manzana", "quantity": 5, "unit_price": 1.2},
        {"id": 2, "name": "Plátano", "quantity": 3, "unit_price": 0.8},
        {"id": 1, "name": "Manzana", "quantity": 1, "unit_price": 1.2}
    ]
    
    for product in products_list:
        ticket.add_product(product, product["quantity"])
    
    assert ticket.total_product_list() == 9.6 




    

    