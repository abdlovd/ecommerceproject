from abc import ABC, abstractmethod
from src.task import Product

class BaseOrder(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def total_sum(self):
        pass

class Order(BaseOrder):
    def __init__(self, product: Product, quantity):
        super().__init__(product.name)
        self.product = product
        self.quantity = quantity

    def total_sum(self):
        return self.product.price * self.quantity
