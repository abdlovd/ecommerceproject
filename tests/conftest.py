import pytest

from src.task import Product, Category
from src.task_iteration import CategoryIteration
from src.category_product import Smartphone, LawnGrass


@pytest.fixture
def read_json_file():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]


@pytest.fixture
def product():
    return Product(
        name="Product 1",
        description="Product 2",
        price = 100.0,
        quantity = 10
    )

@pytest.fixture
def category():
    return Category(
        name="Product 3",
        description="Product 4",
        products= [],
    )


@pytest.fixture
def add_prices():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",180000.0,5)

@pytest.fixture
def add_prices2():
    return Product("Xiaomi Redmi Note 11","1024GB, Синий",31000.0,14)

@pytest.fixture
def category_it(category):
    return CategoryIteration(category)

@pytest.fixture
def product_smartphone1():
    return Smartphone("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",180000.0,5, "fast", "new", 5, "pink")

@pytest.fixture
def product_smartphone2():
    return Smartphone("Samsung", "256GB, Серый цвет",170000.0,2, "slow", "old", 7, "red")

@pytest.fixture
def product_lawngrass1():
    return LawnGrass("Xiaomi Redmi Note 11","1024GB, Синий",31000.0,14, 5, "France", "blue")

@pytest.fixture
def product_lawngrass2():
    return LawnGrass("Xiaomi Redmi Note 12","1024GB, Синий",33000.0,10, 2, "Italy", "green")

@pytest.fixture
def without_product():
    return Product(
        name="Product 99",
        description="Product 99",
        price = 123467.0,
        quantity = 0
    )