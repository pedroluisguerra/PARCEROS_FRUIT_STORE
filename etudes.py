
'''
class Ticket:

    def __init__(self, products_list: list, product_id: int, quantity:int):
        self.products_list = products_list
        self.product_id = product_id
        self.quantity = quantity

    # Add each product and quantity by user getting a subtotal per product 
    def add_product(self):
        for product in self.products_list:
            
            if product["id"] == self.product_id:
                product["quantity"] += self.quantity
                product["subtotal"] += product["unit_price"] * self.quantity

        return self.products_list
    
    # Getting a total for the purchase
    def total_ticket(self):
        total = sum(product["subtotal"] for product in self.products_list)
        return total
'''
'''
class TicketView:
    # Visualizing the products list available in our database
    def __init__(self, product_id, quantity, x: int, y: int, w: int):
        self.product_id = product_id
        self.quantity = quantity
        self.x = x
        self.y = y
        self.w = w

    def paint(self):
        
        text1 = "LIST OF AVAILABLE PRODUCTS"
        locate((DIMENSIONS.w - len(text1)) // 2, self.y, text1)
        text2 = "-------------------------------------------------------------------------------"
        x_1 = (DIMENSIONS.w - len(text2)) // 2
        locate(x_1, self.y + 1, text2)
        locate(x_1, self.y + 2, "| ITEM Nº ")
        locate(x_1 + 11, self.y + 2, "| PRODUCT CODE")
        locate(x_1 + 26, self.y + 2, "|     PRODUCT    ")
        locate(x_1 + 43, self.y + 2, "| UNIT PRICE ")
        locate(x_1 + 56, self.y + 2, "| QUANTITY")
        locate(x_1 + 67, self.y + 2, "| SUBTOTAL |")
        locate(x_1, self.y + 3, text2)


        dao_products = DAO_Product("data\products.db")
        products_list = dao_products.get_all_products()
        ticket = Ticket(products_list, self.product_id, self.quantity)
        purchase = ticket.add_product()                       

        for index, product in enumerate(purchase):
            locate(x_1, self.y + 4 + index, f"|{index + 1:5}.-   |{product['id']:8}      |    {product['name']:10}  | {product['unit_price']:7.2f} €  | {product['quantity']:8.2f} | {product['subtotal']:5.2f} €  |\n")
            
        total_purcharse = ticket.total_ticket()
        locate(x_1, self.y + 4 + len(purchase), text2)
        locate(x_1 + 61, self.y + 5 + len(purchase), f"TOTAL |  {total_purcharse:.2f} €  |\n")
        '''