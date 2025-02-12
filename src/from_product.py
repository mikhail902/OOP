from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def __init__(cls, name, description, price, quantity):
        cls.name = name
        cls.description = description
        cls.price = price
        cls.quantity = quantity
