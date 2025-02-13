from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        return f"{self.name}, {self.__price} руб. Всего {self.quantity} шт"
