from simple_screen import locate, DIMENSIONS, Input, Screen_manager
import sqlite3

class TitleView:
    def __init__(self, texto: str, y: int = 0):
        self.texto = texto
        self.y = y

    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y, self.texto)

class ProductsView:

    def __init__(self, dao_product, x: int, y: int, w: int):
        self.dao_product = dao_product
        self.x = x
        self.y = y
        self.w = w

    def paint(self):
        
        locate(self.x + 15, self.y, "LIST OF AVAILABLE PRODUCTS\n")
        locate(self.x, self.y + 1, "---------------------------------------------------------\n")
        locate(self.x, self.y + 2, "| ITEM Nº ")
        locate(self.x + 11, self.y + 2, "| PRODUCT CODE")
        locate(self.x + 26, self.y + 2, "|     PRODUCT    ")
        locate(self.x + 43, self.y + 2, "| UNIT PRICE |")
        locate(self.x, self.y + 3, "---------------------------------------------------------\n")

        products_list = self.dao_product.get_all_products()

        for product in products_list:
            if not all(key in product for key in ['id', 'name', 'unit_price']):
                raise ValueError("Cada producto debe tener 'id', 'name' y 'unit_price'")
        
        for index, product in enumerate(products_list):
            locate(self.x, self.y + 4 + index, f"|{index + 1:5}.-   | {product['id']:7}      |     {product['name']:10} | {product['unit_price']:6.2f} €   |\n")
            
            return ""

class TicketView:
    def __init__(self, ticket, dao_product, product_id: int, quantity:int, x: int, y: int, w: int):
        self.ticket = ticket
        self.dao_product = dao_product
        self.product_id = product_id  
        self.quantity = quantity
        self.x = x
        self.y = y
        self.w = w

    def paint(self):
        # Encabezado
        locate(self.x + 33, self.y + 14, "YOUR PURCHASE\n")
        locate(self.x, self.y + 15, "-------------------------------------------------------------------------------\n")
        locate(self.x, self.y + 16, "| ITEM Nº ")
        locate(self.x + 11, self.y + 16, "| PRODUCT CODE")
        locate(self.x + 26, self.y + 16, "|     PRODUCT    ")
        locate(self.x + 43, self.y + 16, "| QUANTITY")
        locate(self.x + 54, self.y + 16, "| UNIT PRICE ")
        locate(self.x + 67, self.y + 16, "| SUBTOTAL |\n")
        locate(self.x, self.y + 17, "-------------------------------------------------------------------------------\n")

        # Verificamos si el producto existe en la base de datos
        product = self.dao_product.get_product_by_id(self.product_id)
        if product:
            # Añadimos el producto al ticket
            self.ticket.add_product(product, self.quantity)

            # Iteramos sobre los productos en el ticket y mostramos la información
            for index, (product_id, item) in enumerate(self.ticket.products.items()):
                product = item["product"]
                quantity = item["quantity"]
                unit_price = product["unit_price"]
                subtotal = item["subtotal"]

                locate(self.x, self.y + 18 + index, f"|{index + 1:5}.-   | {product['id']:7}      |     {product['name']:10} | {quantity:5}    | {unit_price:6.2f} €   | {subtotal:5.2f} €  |\n")

            # Total global del ticket
            total = self.ticket.total_product_list()
            locate(self.x, self.y + 19 + len(self.ticket.products), "-------------------------------------------------------------------------------\n")
            locate(self.x + 61, self.y + 20 + len(self.ticket.products), f"TOTAL |  {total:.2f} €  |\n")
        else:
            print("Producto no encontrado en la base de datos.")

    '''
    12345678901234567890123456789012345678901234567890123456789012345678901234567890
    ------------------------------------------------------------------------------
    | ITEM Nº | PRODUCT CODE |     PRODUCT    | QUANTITY | UNIT PRICE | SUBTOTAL |
    '''