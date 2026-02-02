class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data):
        return cls(**data)

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price > new_price:
            print(f"Подтверждаете понижение цены? Введите 'y' если да, 'n' если нет")
            answer = input()
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    def __add__(self, other):
        if type(self) == type(other):
            return self.price*self.quantity + other.price*other.quantity
        raise TypeError


class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.total_categories += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
            for d in self.__products:
                if d.name == product.name:
                    d.quantity += product.quantity
                    if product.price > d.price:
                        d.price = product.price
                        break
        else:
            raise TypeError

    @property
    def products(self):
       return self.__products

    def __str__(self):
        count_product = 0
        for product in self.__products:
            count_product += product.quantity
        return f"{self.name}, количество продуктов: {count_product} шт."
