from src.task import Product, Category
import pytest


def test_task_product(product) -> None:
    assert product.name == "Product 1"
    assert product.description == "Product 2"
    assert product.price == 100.00
    assert product.quantity == 10

def test_task_category(category) -> None:
    assert category.name == "Product 3"
    assert category.description == "Product 4"
    assert category.products == []

def test_add_product(category, product) -> None:
    category.add_product(product)
    product.price = 150
    category.add_product(product)
    assert category.products[0].name == 'Product 1'
    assert category.products[1].name == 'Product 1'

def test_add_product_error(product_smartphone1, category) -> None:
    with pytest.raises(TypeError):
        category.add_product(1)
    with pytest.raises(TypeError):
        result = product_smartphone1 + 1

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
    assert "Цена не должна быть нулевая или отрицательная" in message.out.strip ()
    p.price = 120
    assert p.price == 120

def test_str_category(category):
    assert str(category) == "Product 3, количество продуктов: 0 шт."

def test_product_add(add_prices, add_prices2) -> None:
    assert add_prices + add_prices2 == 1334000.0

def test_str_product(product):
    assert str(product)== "Product 1, 100.0 руб. Остаток: 10 шт."

def test_category_iter(category_it):
    iter(category_it)
    assert category_it.index == 0
    with pytest.raises(StopIteration):
        next(category_it)

def test_average_price(category, without_product):
    assert category.average_price() == 0
    assert without_product.average_price() == 0.0

def test_product_exceptiom(product):
    with pytest.raises(ValueError):
        Product(
            name="кирпич",
            description="новый",
            price=0,
            quantity=0
        )
