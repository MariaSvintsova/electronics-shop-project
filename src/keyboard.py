from src.item import Item

class MixinLang:
    LANGUAGE = "EN"
    def __init__(self):
        self.language = self.LANGUAGE

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: float):
        super().__init__(name, price, quantity)
        self.language = "EN"

    def __str__(self):
        return self.name