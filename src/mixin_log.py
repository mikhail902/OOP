class MixinLog:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"\n{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
