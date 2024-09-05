'''
PARCEROS FRUIT STORE
====================
YOUR BEST OPTION FOR FRUITS!
LIST OF AVAILABLE PRODUCTS     
-------------------------------------------------------------------------------
| ITEM Nº -| PRODUCT CODE-|     PRODUCT    | UNIT PRICE | QUANTITY-| SUBTOTAL |
-------------------------------------------------------------------------------        
|    1.-   |       1      |    Manzana     |    0.50 €  |     0.00 |  0.00 €  |
|    2.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    3.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    4.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    5.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    6.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    7.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    8.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |
|    9.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |  
|   10.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |   
-------------------------------------------------------------------------------
                                                             TOTAL |  1.00 €  |

Please, insert product code or X to finish your purchase:
Please, insert product quantity:

New purchase? (S/N):                                                                                                                                                                                                                                                                                                                                                        YOUR BEST OPTION FOR FRUITS!                                                                                                                                                                      LIST OF AVAILABLE PRODUCTS                                                                                                                                             -------------------------------------------------------------------------------                                                                                                                  | ITEM Nº -| PRODUCT CODE-|     PRODUCT    | UNIT PRICE | QUANTITY-| SUBTOTAL |                                                                                                                  -------------------------------------------------------------------------------                                                                                                                  |    1.-   |       1      |    Manzana     |    0.50 €  |     0.00 |  0.00 €  |                                                                                                                  |    2.-   |       2      |    Plátano     |    0.30 €  |     0.00 |  0.00 €  |                                                                                                                  |    3.-   |       3      |    Naranja     |    0.70 €  |     0.00 |  0.00 €  |                                                                                                                  |    4.-   |       4      |    Uvas        |    1.20 €  |     0.00 |  0.00 €  |                                                                                                                  |    5.-   |       5      |    Lechuga     |    0.90 €  |     0.00 |  0.00 €  |                                                                                                                  |    6.-   |       6      |    Zanahoria   |    0.40 €  |     0.00 |  0.00 €  |                                                                                                                  |    7.-   |       7      |    Tomate      |    0.80 €  |     0.00 |  0.00 €  |                                                                                                                  |    8.-   |       8      |    Patata      |    0.60 €  |     0.00 |  0.00 €  |                                                                                                                  |    9.-   |       9      |    Cebolla     |    0.50 €  |     0.00 |  0.00 €  |                                                                                                                  |   10.-   |      10      |    Pimiento    |    1.00 €  |     1.00 |  1.00 €  |                                                                                                                  -------------------------------------------------------------------------------                                                                                                                  -------------------------------------------------------------TOTAL |  1.00 €  |
'''


from app.models import Ticket, DAO_Product
from app.fronting import TitleView, TicketView
from simple_screen import Screen_manager, Input, cls, Print

title1 = TitleView("PARCEROS FRUIT STORE")
title2 = TitleView("====================", 1)
title3 = TitleView("YOUR BEST OPTION FOR FRUITS!", 3)

dao_products = DAO_Product("data\products.db")
products_list = dao_products.get_all_products()

ticket = Ticket(products_list)
product1 = ticket.add_product(5, 3)
product2 = ticket.add_product(10, 1)
produtc3 = ticket.add_product(2, 2)
product4 = ticket.add_product(5, 1)
ticket_view = TicketView(products_list, 0, 5, 0)

with Screen_manager:
    #cls()
    title1.paint()
    title2.paint()
    title3.paint()
    ticket_view.paint()
    Print()

    Input("Click enter to continue")