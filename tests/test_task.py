from src.task import Product, Category


def test_task_product(product) -> None:
    assert product.name == "Product 1"
    assert product.description == "Product 2"
    assert product.price == 100.00
    assert product.quantity == 10

def test_task_category(category) -> None:
    assert category.name == "Product 3"
    assert category.description == "Product 4"
    assert category.products == ''

def test_add_product(category, product) -> None:
    category.add_product(product)
    product.price = 150
    category.add_product(product)
    assert category.products == 'Product 1, 150 руб. Остаток: 20 шт.\nProduct 1, 150 руб. Остаток: 20 шт.\n'

def test_new_products():
    new_product = Product(name="Product 1", description="Product 2", price=100.00, quantity=10)
    new_product.name = "Product 1"
    new_product.description = "Product 2"
    new_product.__price = 100.00
    new_product.quantity = 10

def test_price(capsys, product):
    p = product
    p.price = 0
    message = capsys.readouterr()
    assert message.out.strip () == "Цена не должна быть нулевая или отрицательная"
    p.price = 120
    assert p.price == 120

def test_str_category(category):
    assert str(category) == "Product 3, количество продуктов: 0 шт."

def test_product_add(add_prices, add_prices2) -> None:
    assert add_prices + add_prices2 == 1334000.0

def test_str_product(product):
    assert str(product)== "Product 1, 100.0 руб. Остаток: 10 шт."

def test_category_iter(test_category_iteration):
    assert test_category_iteration.index == -1
