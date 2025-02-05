import pytest

from src.Product import *


@pytest.fixture()
def telephone_product():
    return Product("Iphone 16", "256GB, Gray space", 150000, 8)


@pytest.fixture()
def new_tel():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    return new_product


@pytest.fixture()
def new_price(telephone_product):
    telephone_product.price = 0


def test_product(telephone_product, new_tel, new_price):
    assert telephone_product.name == "Iphone 16"
    assert telephone_product.price == 150000
    assert telephone_product.quantity == 8
    assert new_tel.price == 180000
    assert new_tel.quantity == 5
    assert new_price is None
