from simple_screen import locate, DIMENSIONS, Input, Screen_manager

class TitleView():

    def __init__(self, texto: str, y: int = 0):
        self.texto = texto
        self.y = y

    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y, self.texto)

class TicketView():

    def __init__(self, ticket, x:int, y:int, w:int):
        self.ticket = ticket
        self.x = x
        self.y = y
        self.w = w

    def paint(self):
        # Encabezado
        locate(self.x, self.y, "-------------------------------------------------------------------------------\n")
        locate(self.x, self.y + 1, "| ITEM Nº ")
        locate(self.x + 11, self.y + 1, "| PRODUCT CODE")
        locate(self.x + 26, self.y +1, "|     PRODUCT    ")
        locate(self.x + 43, self.y + 1, "| QUANTITY")
        locate(self.x + 54, self.y + 1, "| UNIT PRICE ")
        locate(self.x + 67, self.y + 1, "| SUBTOTAL |\n")
        locate(self.x, self.y + 2, "-------------------------------------------------------------------------------\n")

        # Detalles del producto
        for index, item in enumerate(self.ticket.products.values()):
            product = item["product"]
            quantity = item["quantity"]
            unit_price = product["unit_price"]
            subtotal = item["subtotal"]

            locate(self.x, self.y + 3 + index, f"|{index + 1:5}.-   | {product['id']:7}      |     {product['name']:10} | {quantity:5}    | {unit_price:6.2f} €   | {subtotal:5.2f} €  |\n")

        # Total global del ticket
        total = self.ticket.total_product_list()
        locate(self.x, self.y + 3 + len(self.ticket.products), "-------------------------------------------------------------------------------\n")
        locate(self.x, self.y + 4 + len(self.ticket.products), f"TOTAL: {total:.2f} €\n")

        return ""


    ''''
    12345678901234567890123456789012345678901234567890123456789012345678901234567890
    ------------------------------------------------------------------------------
    | ITEM Nº | PRODUCT CODE |     PRODUCT    | QUANTITY | UNIT PRICE | SUBTOTAL |
    '''