from simple_screen import locate, DIMENSIONS, Input

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
      
      locate(self.x, self.y, "| PRODUCT CODE")
      locate(self.x + 20 , self.y, "| PRODUCT      ")
      locate(self.x + 50 , self.y, "| QUANTITY")
      locate(self.x + 70 , self.y, "| UNIT PRICE ")
      locate(self.x + 90 , self.y, "| SUBTOTAL\n")
      locate(self.x, self.y + 1,"----------------------------------------------------\n")
      
      for item in self.products.values():
            product = item["product"]
            quantity = item["quantity"]
            unit_price = product["unit_price"]
            subtotal = item["subtotal"]
            
            # Formateamos cada línea del producto
            ticket_view += f"{product['id']:6} | {product['name']:12} | {quantity:8} | {unit_price:9.2f} € | {subtotal:9.2f} €\n"

        # Total global del ticket
      total = self.total_product_list()
      ticket_view += "----------------------------------------------------\n"
      ticket_view += f"TOTAL: {total:.2f} €\n"
        
      return ticket_view
    
    