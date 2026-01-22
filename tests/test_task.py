def test_task_product() -> None:
    assert products.name == "Product 1"
    assert products.description == "Product 2"
    assert products.price == "100"
    assert products.quantity == 10

def test_task_category() -> None:
    assert category.name == "Product 3"
    assert category.description == "Product 4"
    assert category.products == "Product 5"