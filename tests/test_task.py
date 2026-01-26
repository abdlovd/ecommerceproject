from src.task import Product


def test_task_product(product) -> None:
    assert product.name == "Product 1"
    assert product.description == "Product 2"
    assert product.price == "100"
    assert product.quantity == 10

def test_task_category(category) -> None:
    assert category.name == "Product 3"
    assert category.description == "Product 4"
    assert category.products == "Product 5"

def test_add_products(category) -> None:
    assert category.products == 'Product 5'

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