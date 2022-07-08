#OOP
class Item:
    def item_details(self, xname, xprice, xquantity ):
        return xprice * xquantity
        
        
    
item1 = Item()
item1.name = "Phone"
item1.price = 250
item1.quantity = 500
print(item1.item_details(item1.name, item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 500
item2.quantity = 10
print(item2.item_details(item2.name, item2.price, item2.quantity))


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def item_details(self ):
        return self.price * self.quantity
    
    def item_name(self):
        self.name = "Laptop"
        
    def item_price(self):
        self.price = 150
        
    def item_quantity(self):
        self.quantity = 10
        
item = Item()
print(item.item_details())