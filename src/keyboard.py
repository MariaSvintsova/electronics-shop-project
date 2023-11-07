from src.item import Item

class MixinLang:
    LANGUAGE = "EN"
    def __init__(self):
        self.__language = self.LANGUAGE

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: float):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)

    def __str__(self):
        return self.name

