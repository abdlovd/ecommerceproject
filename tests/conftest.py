import pytest

from src.task import Product, Category


@pytest.fixture
def products():
    return Product(
        name="Product 1",
        description="Product 2",
        price="100",
        quantity=10
    )

@pytest.fixture
def category():
    return Category(
        name="Product 3",
        description="Product 4",
        products="Product 5",
    )
