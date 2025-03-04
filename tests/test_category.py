import pytest

from src.category import *
from src.product import *

prod1 = Product("Watermelon", "from china", 300, 10)
prod2 = Product("lemon", "Pakistan", 400, 8)
prod3 = Product("Pineapple", "Thai", 600, 14)


@pytest.fixture()
def prod():
    return Category(
        "Продукты",
        "Свежие продукты с разных стран",
        [prod1, prod2, prod3],
    )


@pytest.fixture()
def add_prod(prod):
    prod4 = Product("Banana", "Africa", 300, 20)
    prod.add_product(prod4)
    return prod


@pytest.fixture()
def nul_category():
    return Category(
        "0",
        "0",
        [],
    )


def test_category(prod, add_prod, nul_category):
    assert Category.category_count == 2
    assert prod1.price == 300
    assert prod3.quantity == 14
    assert add_prod.product_count == 4
    assert str(prod) == "Продукты, количество продуктов: 52 шт"
    prod4 = Product("apple", "Russia", 400, 20)
    prod.add_product(prod4)
    assert (
        prod.products
        == """Watermelon, 300 руб. Остаток: 10 шт\nlemon, 400 руб. Остаток: 8 шт\nPineapple, 600 руб. Остаток: 14 шт\nBanana, 300 руб. Остаток: 20 шт\napple, 400 руб. Остаток: 20 шт\n"""
    )
    assert str(prod) == "Продукты, количество продуктов: 72 шт"
    assert prod.middle_price() == 400
    assert nul_category.middle_price() == 0
