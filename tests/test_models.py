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
    


def test_add_product_ticket():
    ticket = Ticket()
    dao = DAO_Product(r"data\products.db")
    product_list = dao.get_all_products()

    product = next((p for p in product_list if p["id"] == 2), None)
    #assert product is not None, "El producto con el ID informado no existe en la lista de productos"
    
    ticket.add_product(product, 2)
    assert ticket.products[2]["quantity"] == 2
    assert ticket.products[2]["subtotal"] == 0.6

    product = next((p for p in product_list if p["id"] == 8), None)
    #assert product is not None, "El producto con el ID informado no existe en la lista de productos"
    
    ticket.add_product(product, 3)
    assert ticket.products[8]["quantity"] == 3
    assert round(ticket.products[8]["subtotal"],2) == 1.8

    



    

    