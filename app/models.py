from abc import ABC
import sqlite3

class Product:

    #Esta clase compara con def __eq__ si nuestros productos son iguales.

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
    #En esta clase DAO la usamos como una interface/contrado para los productos, sólo trabajamos la opción de obtener todos los productos de la base de datos.
    def get_all_products(self):
        pass

class DAO_Product(DAO):

    #Siguiendo la teoria en clase, con este DAO construimos nuestra lista de diccionarios para generar la simulación de un ticket de caja.

    def __init__(self, path):
        self.path = path        

    def get_all_products(self):
        # Obtiene una lista de diccionarios que se usará para gestionar la simulación

        try:

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
    
        except sqlite3.OperationalError as e:
            return f'Error connecting to database, please contact database administrator'
    
    def get_product_by_id(self, product_id: int):

        # Esta función la desarrollé por curiosidad propia porque quería que la simulación verifique en la base de datos el código que el usuario introdujera.

        try:
            conn = sqlite3.connect(self.path)
            cur = conn.cursor()
            cur.execute("SELECT id, name, unit_price FROM products WHERE id = ?", (product_id,))
            row = cur.fetchone()
            conn.close()

            if row:
                
                return {
                            "id": row[0],
                            "name": row[1],
                            "unit_price": row[2]
                        }
            else:
                return False
        
        except sqlite3.OperationalError as e:
            return f'Error connecting to database, please contact database administrator'        

class Ticket:
    # Esta clase gestionará todas las operaciones en la compra, agregar productos, cantidades, subtotal y total en la compra.

    def __init__(self, products_list: list):
        self.products_list = products_list
        
    def add_product(self, product_id, quantity):
        #Agrega producto por su id y actualiza la cantidad en la lista de diccionarios.

        for product in self.products_list:
            
            if product["id"] == product_id:
                product["quantity"] += quantity
                product["subtotal"] += product["unit_price"] * quantity

        return self.products_list
    
    
    def total_ticket(self):
        #Obtiene el total de toda la compra a través de la clave subtotal.

        total = sum(product["subtotal"] for product in self.products_list)
        return total
         