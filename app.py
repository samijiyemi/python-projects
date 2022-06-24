class Product:

    """_summary_
    """

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative!")
        self.__price(value)


product = Product(-50)
print(product.price)
