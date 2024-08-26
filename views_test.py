from app.models import Ticket, DAO_Product
from app.fronting import TitleView, TicketView
from simple_screen import Screen_manager, Input, cls, Print

title1 = TitleView("PARCEROS FRUIT STORE")
title2 = TitleView("YOUR BEST OPTION FOR FRUITS", 2)
ticket = Ticket()
ticket.add_product({"id": 1, "name": "Apple", "unit_price": 0.50}, 4)
ticket.add_product({"id": 2, "name": "Banana", "unit_price": 0.30}, 1)
ticket.add_product({"id": 3, "name": "Orange", "unit_price": 0.80}, 1.5)
ticket_view = TicketView(ticket,0,5,0)



with Screen_manager:
    cls()
    title1.paint()
    title2.paint()
    ticket_view.paint()
    Print()

    Input("Click enter to continue")

