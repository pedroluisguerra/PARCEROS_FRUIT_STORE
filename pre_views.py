from app.models import Ticket, DAO_Product
from app.fronting import TitleView, TicketView
from simple_screen import Screen_manager, Input, cls, Print

title1 = TitleView("PARCEROS FRUIT STORE")
title2 = TitleView("====================", 1)
title3 = TitleView("YOUR BEST OPTION FOR FRUITS!", 3)

ticket_view1 = TicketView(0, 0, 0, 5, 0)
#ticket_view2 = TicketView(10, 1, 0, 4, 0)

#ticket = Ticket()
#ticket_view1 = TicketView(ticket, dao_product, 2, 1, 0, 5, 0)
#ticket_view2 = TicketView(ticket, dao_product, 10, 2, 0, 5, 0)
#ticket_view3 = TicketView(ticket, dao_product, 5, 6, 0, 5, 0)
#ticket_view4 = TicketView(ticket, dao_product, 2, 2, 0, 5, 0)

with Screen_manager:
    cls()
    title1.paint()
    title2.paint()
    title3.paint()
    ticket_view1.paint()
    #ticket_view2.paint()
    Print()

    Input("Click enter to continue")