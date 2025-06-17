class Item:
    pay_rate = 0.8 #Pay rate after 20% discount
    all = []
    
    def __init__(self, name : str, price : float, quantity=0):
        # Run operations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero."
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero."
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
        
    def apply_discount(self):
        self.price = self,price * self.pay_rate

item1 = Item("Phone", 10000, 5)

item2 = Item("Laptop", 50000, 10)
item2.pay_rate = 0.7

item3 - Item("Cable", 100, 7)
