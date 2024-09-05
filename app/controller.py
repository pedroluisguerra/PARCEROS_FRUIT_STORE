from app.fronting import *
from app.models import *
from simple_screen import DIMENSIONS, locate, Input, cls, Screen_manager

class FruitStore:

    def __init__(self):

        #TRY

        self.title1 = TitleView("PARCEROS FRUIT STORE")
        self.title2 = TitleView("====================", 1)
        self.title3 = TitleView("YOUR BEST OPTION FOR FRUITS!", 3)
        
        self.dao_products = DAO_Product("data\products.db")
        self.products_list = self.dao_products.get_all_products()
        self.purchase = Ticket(self.products_list)
        self.ticket_view = TicketView(self.products_list, 0, 5)
        text1 = "Please, insert product code or X to finish your purchase: "
        text2 = "Please, insert product quantity: "
        text3 = "New purchase? (S/N): "
        x1 = ((DIMENSIONS.w - len(text1)) // 2) - 9
        y1 = len(self.products_list) + 13
        self.insert_product = InputProduct(text1, x1, y1)
        self.insert_quantity = InputQuantity(text2, x1, y1 + 2)
        self.keep_purchase = InputViewSN(text3, x1, y1 + 3)     

        #EXCEPT - sqlite3.OperationalError

    def run(self):
        with Screen_manager:
            while True:
                cls()
                self.title1.paint()
                self.title2.paint()
                self.title3.paint()
                self.ticket_view.paint()
                product = self.insert_product.paint()
                quantity = self.insert_quantity.paint()
                if product == "X" or product == "":
                    check_continue = self.keep_purchase.paint()
                    if check_continue.upper() == "S":
                        self.purchase = Ticket(self.products_list)
                        self.purchase.products_list = self.products_list
                        continue
                    else:
                        break

                product = int(product)
                quantity = int(quantity)
                self.purchase.add_product(product, quantity)

            Input("Click Enter to exit.")

        



