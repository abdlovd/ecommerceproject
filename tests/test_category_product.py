import pytest


def test_smartphone(product_smartphone1):
    assert product_smartphone1.name == 'Samsung Galaxy C23 Ultra'
    assert product_smartphone1.description == '256GB, Серый цвет, 200MP камера'
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 'fast'
    assert product_smartphone1.model == 'new'
    assert product_smartphone1.memory == 5
    assert product_smartphone1.color == 'pink'

def test_add_smartphones(product_smartphone1, product_smartphone2):
    assert product_smartphone1 + product_smartphone2 == 1240000.0

def test_add_smartphones_error(product_smartphone1, product_smartphone2):
    with pytest.raises(TypeError):
        result = product_smartphone1 + 1

def test_lawngrass1(product_lawngrass1):
    assert product_lawngrass1.name == 'Xiaomi Redmi Note 11'
    assert product_lawngrass1.description == '1024GB, Синий'
    assert product_lawngrass1.price == 31000.0
    assert product_lawngrass1.quantity == 14
    assert product_lawngrass1.germination_period == 5
    assert product_lawngrass1.country == "France"
    assert product_lawngrass1.color == "blue"

def test_add_lawngrass(product_lawngrass1, product_lawngrass2):
    assert product_lawngrass1 + product_lawngrass2 == 764000.0

def test_add_lawngrass_error(product_lawngrass1, product_lawngrass2):
    with pytest.raises(TypeError):
        result = product_lawngrass1 + 1
