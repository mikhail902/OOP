from src.Category import *


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток {self.quantity} шт"

    def __add__(self, other):
        if type(self) == type(other):
            first_product = self.__price * self.quantity
            second_product = other.__price * other.quantity
            return first_product + second_product
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_prod):
        if issubclass(Category, (Smartphone, LawnGrass)):
            name, description, price, quantity = "", "", 0, 0
            for key, value in new_prod.items():
                if key == "name":
                    name = value
                if key == "description":
                    description = value
                if key == "price":
                    price = value
                if key == "quantity":
                    quantity = value
            new_prod = cls(name, description, price, quantity)
            return new_prod
        else:
            return "Этот продукт нельзя добавить в список продуктов"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new):
        if new < 0 or new == 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    colour: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, colour
    ):
        super().__init__(self, name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.colour = colour


class LawnGrass(Product):
    country: str
    germination_period: str
    colour: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, colour
    ):
        super().__init__(self, name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.colour = colour
