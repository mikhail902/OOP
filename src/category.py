from src.product import *


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, prod):
        if isinstance(prod, Product):
            self.__products.append(prod)
            self.product_count += 1
        else:
            raise TypeError(f"Добавлять можно только обьекты Product, {prod}")

    def __str__(self):
        sum_quantity = 0
        for prod in self.__products:
            sum_quantity += prod.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт"

    def middle_price(self):
        try:
            sum_price = 0
            amount = 0
            for prod in self.__products:
                sum_price += prod.price
                amount += 1
            return round(sum_price / amount, 2)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        str_products = ""
        for prod in self.__products:
            str_products += (
                f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт\n"
            )
        return str_products
