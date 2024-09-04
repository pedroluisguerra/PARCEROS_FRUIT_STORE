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


def test_add_product():
    products_list = [
        {"id": 1, "name": "Manzana", "unit_price": 1.2, "quantity": 1, "subtotal": 1.2},
        {"id": 2, "name": "Plátano", "unit_price": 0.8, "quantity": 0, "subtotal": 0},
        {"id": 3, "name": "Naranja", "unit_price": 1.2, "quantity": 2, "subtotal": 2.4}
    ]

    ticket = Ticket(products_list)
    purchase1 = ticket.add_product(2, 2)       
    assert purchase1[1]["quantity"] == 2
    assert purchase1[1]["subtotal"] == 1.6
   
    purchase2 = ticket.add_product(3 , 3)
    assert purchase2[2]["quantity"] == 5
    assert purchase2[2]["subtotal"] == 6

    
    purchase = ticket.add_product(1, 1)
    assert purchase[0]["quantity"] == 2
    assert purchase[0]["subtotal"] == 2.4

    assert ticket.total_ticket() == 10 

   