class Product:
    def __init__(self, name, id, price, quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity


berries = Product("Raspberries", 1, 20.0, 50)
fruits = Product("Apples", 2, 15.0, 100)
vegetables = Product("Tomatoes", 3, 2.0, 20)

class Inventory:
    def __init__(self, products, sum):
        self.products = []
        self.sum = sum

    def add_inventory(self, product):
        self.products.append(product)

    def sum_up_value(self):
        value = 0
        for product in self.products:
            value += (product.get_price() * float(product.get_quantity()))
        return value

    def remove_inventory(self, product):
        self.products.remove(product)



inventory = Inventory('Inventory', 0)
inventory.add_inventory(berries)
inventory.add_inventory(fruits)
inventory.add_inventory(vegetables)

print(inventory.products[0].name)
print(inventory.sum_up_value())

print(inventory.products[1].name)
print(inventory.sum_up_value())

print(inventory.products[2].name)
print(inventory.sum_up_value())

inventory.remove_inventory(vegetables)
print(inventory.products[1].id)
print(inventory.products[0].price)
print(inventory.sum_up_value())
