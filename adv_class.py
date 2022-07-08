         
class Item:
    #Instance attribute
    pay_rate = 0.8 #Discount rate
    all = []  #Pass all instances into a list
    
    #defined the arguments but only be called if no corresponding attribute is passed ab inition
    def __init__(self, name: str, price:float=200, quantity=1): #==> Given permanent datatype to argument
        
        #Used assert to ensure that no attribute received below 0
        assert price >= 0, f"Price {price} must be 0 or above"
        assert quantity >= 0, f"Quantity {quantity} must be 0 or above"

        #To call in the instance into the class
        Item.all.append(self)
        
        #Assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity
    
    def price_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = f"The after a discount you pay : {self.price * self.pay_rate}"  #convert pay rate to self to become global

    #List all instances with their attributes in a list
    def __repr__(self):
        return f"'{self.name}': {self.price}, {self.quantity}"
        #return f"Item('{self.name}'): {self.price}, {self.quantity}"
    
item1 = Item("Charger", 500, 5 )
item2 = Item("iMac", 500, 15)
item3 = Item("Phone", 100, 1)
item4 = Item("Laptop", 1000, 3)
item5 = Item("Cable", 10, 5)
item6 = Item("Mouse", 50, 5)
item7 = Item("Keyboard", 75, 5)

print(Item.all)

    