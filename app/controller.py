from app.fronting import *
from app.models import *
from simple_screen import DIMENSIONS, locate, Input, cls, Screen_manager

class FruitStore:

    def __init__(self):
        self.title1 = TitleView("PARCEROS FRUIT STORE")
        self.title2 = TitleView("====================", 1)
        self.title3 = TitleView("YOUR BEST OPTION FOR FRUITS!", 3)
'''
dao_products = DAO_Product("data\products.db")
        products_list = dao_products.get_all_products()
        '''
        
    def run(self):
        pass



