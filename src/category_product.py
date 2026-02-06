from src.task import Product


class Smartphone(Product):
    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

    def __init__(self, name, description, price, quantity, germination_period, country, color):
        super().__init__(name, description, price, quantity)
        self.germination_period = germination_period
        self.country = country
        self.color = color

