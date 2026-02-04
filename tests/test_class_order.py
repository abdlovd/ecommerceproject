from src.class_order import Order
from src.task import Product

def test_class_order():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    order1 = Order(product, 1)
    order2 = Order(product, 2)
    assert order1.total_sum() == 180000.0
    assert order2.total_sum() == 360000.0
