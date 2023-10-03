import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.

        :return: Цена товара после применения скидки.
        """
        self.price *= self.pay_rate


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls, filename) -> None:
        """
        Класс-метод инициализирует экземпляры класса Item из файла src/items.csv

        """
        # Очищение списка all перед наполнением экземплярами из файла
        cls.all = []
        with open(filename, encoding='utf-8') as csvfile:
            all_lines = csv.DictReader(csvfile)
            for row in all_lines:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(stringnumber) -> int:
        """
        Статический метод, возвращающий число из числа-строки

        :return: число
        """
        return int(float(stringnumber))







