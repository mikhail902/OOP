import pytest
from src.Product import *


@pytest.fixture()
def telephone_product():
    return Product("Iphone 16", "256GB, Gray space", 150000, 8)


def test_product(telephone_product):
    assert telephone_product.name == "Iphone 16"
    assert telephone_product.price == 150000
    assert telephone_product.quantity == 8
