from abc import ABC, abstractmethod
import sqlite3


class Product:

    @classmethod

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
    '''
    @abstractmethod
    def save_product(self,instancia):
        pass

    @abstractmethod
    def update_product(self,):
        pass

    @abstractmethod
    def delete_product(self):
        pass

    @abstractmethod
    def check_product(self):
        pass
    '''

    @abstractmethod
    def get_all_products(self):
        pass

class DAO_Product(DAO):

    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(self.path)

    def __del__(self):
        self.conn.close()

    def get_all_products(self):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("SELECT id, name, unit_price FROM products")
                products_list = []
                for row in cursor.fetchall():
                    product = Product(*row)
                    products_list.append({
                        "id": row[0],
                        "name": row[1],
                        "unit_price": row[2]
                    })
                return products_list

        except sqlite3.Error as e:
            print(f"Error accessing database: {e}")
            return []
        
    def get_product_by_id(self, product_id: int):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("SELECT id, name, unit_price FROM products WHERE id = ?", (product_id,))
                row = cursor.fetchone()
                if row:
                    return {
                        "id": row[0],
                        "name": row[1],
                        "unit_price": row[2]
                    }
                else:
                    return None
        except sqlite3.Error as e:
            print(f"Error accessing database: {e}")
            return None

class Ticket:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product["id"] in self.products:
            self.products[product["id"]]["quantity"] += quantity
        else:
            self.products[product["id"]] = {
                "product": product,
                "quantity": quantity
            }
        self.products[product["id"]]["subtotal"] = self.products[product["id"]]["quantity"] * product["unit_price"]

    def update_quantities(self, products_list):
        for product in products_list:
            self.add_product(product, product["quantity"])

    def total_product_list(self):
        total = 0
        for item in self.products.values():
            total += item["subtotal"]
        return total
         