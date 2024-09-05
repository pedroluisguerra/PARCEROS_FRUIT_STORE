from simple_screen import locate, DIMENSIONS, Input, Screen_manager
from app.models import Ticket, DAO_Product
import sqlite3

class TitleView:
    # Esta clase "visualiza" los titulos de la pantalla en la simulación.
     
    def __init__(self, texto: str, y: int = 0):
        self.texto = texto
        self.y = y

    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y, self.texto)

class TicketView:
    # Visualiza la lista de productos y el detalle de la compra.

    def __init__(self, products_list:list, x: int, y: int):
        self.products_list = products_list
        self.x = x
        self.y = y

    def paint(self):
        
        text1 = "LIST OF AVAILABLE PRODUCTS"
        locate((DIMENSIONS.w - len(text1)) // 2, self.y, text1)
        text2 = "-" * 79
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
        locate(x_1 + 61, self.y + 5 + len(self.products_list), f"TOTAL | {total_purcharse:5.2f} €  |\n")
        
class InputView:
    #Visualiza las entradas que dará el usuario en la compra.

    def __init__(self, text: str, x: int, y: int):
        self.text = text
        self.y = y
        self.x = x
        self.value = ""

    def paint(self):
        locate(self.x, self.y, self.text)
        return Input()
    
class InputProduct(InputView):

    #Visualiza y gestiona el dato de código del producto que ingresa el usuario, haciendo las debidas verificaciones.

    def paint(self):
        while True:
            id_by_user = super().paint()

            if id_by_user.upper() == "X":
                return str("X")

            try:
                product_id = int(id_by_user)
                dao_products = DAO_Product("data\products.db")
                product_found = dao_products.get_product_by_id(product_id)

                if product_id <= 0:
                    locate(self.x, self.y + 1, f'Invalid code. insert only a product code shown on LIST OF AVAILABLE PRODUCTS or insert X to finish your purchase.')
                            
                if product_found and isinstance(product_found, dict) and product_found.get("id") == product_id:
                    locate(self.x, self.y + 1, " " * 113)
                    return product_id                
                
                else:
                    locate(self.x, self.y + 1, f'Invalid code. insert only a product code shown on LIST OF AVAILABLE PRODUCTS or insert X to finish your purchase.')
                    
            except ValueError:

                locate(self.x, self.y + 1, f'Invalid code. insert only a product code shown on LIST OF AVAILABLE PRODUCTS or insert X to finish your purchase.')
                

class InputQuantity(InputView):

    #Visualiza y gestiona el dato de cantidad del producto que ingresa el usuario, haciendo las debidas verificaciones.

    def paint(self):
        while True:

            quantity_by_user = super().paint()

            try:
                quantity = int(quantity_by_user)
                
                if quantity <= 0:
                    locate(self.x, self.y + 1, f'Quantity cannot be negative nor zero nor letter, only a positive integer')

                if quantity > 0:

                    locate(self.x, self.y + 1, " " * 113)
                    return quantity
                
            except ValueError:

                locate(self.x, self.y + 1, f'Quantity cannot be negative nor zero nor letter, only a positive integer')

class InputViewSN(InputView):
        pass

print(__name__)
if __name__ == "__main__":

    with Screen_manager:
        
        dao_products = DAO_Product("data\products.db")
        products_list = dao_products.get_all_products()

        ticket = Ticket(products_list)
        product1 = ticket.add_product(5, 3)
        product2 = ticket.add_product(10, 1)
        produtc3 = ticket.add_product(2, 2)
        product4 = ticket.add_product(5, 1)

        ticket_view = TicketView(products_list, 0, 0, 0)
        insert_product_view = InputView("Please, insert product code: ", 0, 20)
        inser_quantity_view = InputView("Please, insert quantity: ", 0, 21)

        ticket_view.paint()
        insert_product_view.paint()
        inser_quantity_view.paint()

        Input("Please, click Enter to finish.")