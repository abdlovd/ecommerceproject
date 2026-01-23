def test_task_product(product) -> None:
    assert product.name == "Product 1"
    assert product.description == "Product 2"
    assert product.price == "100"
    assert product.quantity == 10

def test_task_category(category) -> None:
    assert category.name == "Product 3"
    assert category.description == "Product 4"
    assert category.products == "Product 5"
    