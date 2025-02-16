class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} cannot be negative!"
        assert quantity >= 0, f"quantity {quantity} cannot be negative!"
       
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
        
    def apply_discount(self):
        self.price = self.price * self.pay_rate
     
    # represent an object    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

item1.apply_discount()
item2.pay_rate = 0.7
item2.apply_discount()
item2.has_numpad = False

# print(Item.__dict__) # all the attributes for class level
# print(item1.__dict__) # all the attributes for instance level

print(Item.all)
