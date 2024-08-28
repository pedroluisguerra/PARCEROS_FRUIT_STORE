from app.models import Ticket, DAO_Product
from app.fronting import TitleView, TicketView, ProductsView
from simple_screen import Screen_manager, Input, cls, Print

title1 = TitleView("PARCEROS FRUIT STORE")
title2 = TitleView("YOUR BEST OPTION FOR FRUITS", 2)

dao_product = DAO_Product("data/products.db")

products_list_view = ProductsView(dao_product, 0, 4, 0)

ticket = Ticket()
ticket_view1 = TicketView(ticket, dao_product, 2, 1, 0, 5, 0)
ticket_view2 = TicketView(ticket, dao_product, 10, 2, 0, 5, 0)
ticket_view3 = TicketView(ticket, dao_product, 5, 8, 0, 5, 0)

with Screen_manager:
    cls()
    title1.paint()
    title2.paint()
    products_list_view.paint()
    ticket_view1.paint()
    ticket_view2.paint()
    ticket_view3.paint()
    Print()

    Input("Click enter to continue")