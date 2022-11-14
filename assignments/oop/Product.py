
class Product:
 # init method or constructor
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantiy = quantity

    def sayHello(self):
        print('Product:', self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantiy)