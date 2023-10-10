from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim


    def __add__(self, other):
        if isinstance(self.__class__, Item.__class__):
            return self.quantity + other.quantity
        elif isinstance(self.__class__, Phone.__class__):
            return self.quantity + other.quantity
        raise TypeError("Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if isinstance(number, int) and number > 0:
            self._number_of_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")