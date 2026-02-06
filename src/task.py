from src.print_mixin import PrintMixin
from src.base_product import BaseProduct

class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, data):
        """создать класс-метод new_product, который будет принимать на вход параметры
         товара в словаре и возвращать созданный объект класса Product."""
        return cls(**data)

    @property
    def price(self):
        return self.__price

    def __str__(self):
        """вернуть возможность просмотра товаров, нужно реализовать геттер,
        который будет выводить список товаров в виде строк"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    @price.setter
    def price(self, new_price):
        """В сеттере реализуйте проверку: в случае если цена равна или ниже нуля"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            print(f"Подтверждаете понижение цены? Введите 'y' если да, 'n' если нет")
            answer = input()
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    def __add__(self, other):
        """ В Итоге у вас получалась полная стоимость всех товаров на складе."""
        if type(self) == type(other):
            return self.price*self.quantity + other.price*other.quantity
        raise TypeError


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    """Количество категории"""
    product_count = 0
    """Количество товаров"""

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """Для добавления товаров в категорию реализуйте специальный метод add_product()
        в классе Category, в который нужно передавать объект класса Product
        и уже его записывать в приватный атрибут списка товаров."""
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
