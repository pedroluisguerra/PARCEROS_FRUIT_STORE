from simple_screen import locate, DIMENSIONS, Input, Screen_manager
from app.models import Ticket, DAO_Product
import sqlite3

class TitleView:
    # Main title 
    def __init__(self, texto: str, y: int = 0):
        self.texto = texto
        self.y = y

    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y, self.texto)

class TicketView:
    # Visualizing the products list available in our database
    def __init__(self, products_list:list, x: int, y: int, w: int):
        self.products_list = products_list
        self.x = x
        self.y = y
        self.w = w

    def paint(self):
        
        text1 = "LIST OF AVAILABLE PRODUCTS"
        locate((DIMENSIONS.w - len(text1)) // 2, self.y, text1)
        text2 = "-------------------------------------------------------------------------------"
        x_1 = (DIMENSIONS.w - len(text2)) // 2
        locate(x_1, self.y + 1, text2)
        locate(x_1, self.y + 2, "| ITEM Nº ")
        locate(x_1 + 11, self.y + 2, "| PRODUCT CODE")
        locate(x_1 + 26, self.y + 2, "|     PRODUCT    ")
        locate(x_1 + 43, self.y + 2, "| UNIT PRICE ")
        locate(x_1 + 56, self.y + 2, "| QUANTITY")
        locate(x_1 + 67, self.y + 2, "| SUBTOTAL |")
        locate(x_1, self.y + 3, text2)     
                           

        for index, product in enumerate(self.products_list):
            locate(x_1, self.y + 4 + index, f"|{index + 1:5}.-   |{product['id']:8}      |    {product['name']:10}  | {product['unit_price']:7.2f} €  | {product['quantity']:8.2f} | {product['subtotal']:5.2f} €  |\n")

        total_purcharse = sum(product["subtotal"] for product in self.products_list)
        locate(x_1, self.y + 4 + len(self.products_list), text2)
        locate(x_1 + 61, self.y + 5 + len(self.products_list), f"TOTAL |  {total_purcharse:.2f} €  |\n")
        
class InputView:

    def __init__(self, etiqueta: str, x: int, y: int):
        self.etiqueta = etiqueta
        self.y = y
        self.x = x
        self.value = ""

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        return Input()
    
class Input_Product(InputView):

    def paint(self):
        while True:
            id = super().paint()
            try:
                product_id = int(id)
                dao_products = DAO_Product("data\products.db")
                product_found = dao_products.get_product_by_id(product_id)
                if product_found[0] == product_id:
                    return product_id
            except ValueError as e:
                if id <= 0 or id == "" or id == str or id :
                    return id
                locate(self.x, self.y + 1, "Please, insert only a number shown on LIST OF AVAILABLE PRODUCTS or insert X to finish your purchase")