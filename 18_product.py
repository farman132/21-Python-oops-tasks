class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print(p.price)
p.price = 200
print(p.price)
del p.price
