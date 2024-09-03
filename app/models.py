from abc import ABC
import sqlite3


class Product:

    def __init__(self, id: int, name: str, unit_price: float):
        self.id = id
        self.name = name
        self.unit_price = unit_price

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):                        
            return self.id == other.id and self.name == other.name and self.unit_price == other.unit_price
        return False
    
    def __hash__(self) -> int:
        return hash(self.id, self.name, self.unit_price)

    def __repr__(self) -> str:
        return f"Product ({self.id}): {self.name}" 

class DAO(ABC):
    def get_all_products(self):
        pass

class DAO_Product(DAO):

    def __init__(self, path):
        self.path = path
        

    # Getting all products in a list of dictionaries
    def get_all_products(self):

        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute("SELECT id, name, unit_price FROM products")
        products_list = []
        for row in cur.fetchall():
            products_list.append({
                "id": row[0],
                "name": row[1],
                "unit_price": row[2],
                "quantity": 0,
                "subtotal": 0
                })
        
        conn.close()

        return products_list

    # Verify if a product id inserted by user is in our database     
    def get_product_by_id(self, product_id: int):
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute("SELECT id, name, unit_price FROM products WHERE id = ?", (product_id,))
        row = cur.fetchone()
        if row:
            conn.close()
            return True
        else:
            conn.close()
            return False

class Ticket:

    def __init__(self, products_list: list, product_id: int, quantity:int):
        self.products_list = products_list
        self.product_id = product_id
        self.quantity = quantity

    # Add each product and quantity by user getting a subtotal per product 
    def add_product(self):
        for product in self.products_list:
            
            if product["id"] == self.product_id:
                product["quantity"] += self.quantity
                product["subtotal"] += product["unit_price"] * self.quantity

        return self.products_list
    
    # Getting a total for the purchase
    def total_ticket(self):
        total = sum(product["subtotal"] for product in self.products_list)
        return total
         