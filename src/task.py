class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        for product in products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if self.__price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price > new_price:
            print(f"Подтверждаете понижение цены? Введите 'y' если да, 'n' если нет")
            answer = input()
            if answer == "y":
                self.__price = new_price
            return
        self.__price = new_price

class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, name, description, price, quantity):
        self.__products.append(Product(name, description, price, quantity))

    @property
    def products(self):
        return self.__products

    @property
    def products_ (self):
        products_str = " "
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
