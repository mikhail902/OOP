import pytest

from src.Category import *
from src.Product import *

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


def test_category(prod, add_prod):
    assert Category.category_count == 1
    assert prod1.price == 300
    assert prod3.quantity == 14
    assert add_prod.product_count == 4
    assert str(prod) == "Продукты, количество продуктов: 52 шт"
