from app.fronting import *
from app.models import *
from simple_screen import DIMENSIONS, locate, Input, cls, Screen_manager

class FruitStore:

    def __init__(self):
        self.title1 = TitleView("PARCEROS FRUIT STORE")
        self.title2 = TitleView("YOUR BEST OPTION FOR FRUITS", 2)

        self.ticket_view = TicketView([],0,5,0)
        self.dao_product = DAO_Product("data/products.db")

    def run(self):
        pass



