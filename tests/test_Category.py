from src.Category import *
import pytest
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


def test_category(prod):
    assert Category.category_count == 1
    assert prod1.price == 300
    assert prod3.quantity == 14
