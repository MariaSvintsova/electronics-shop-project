"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item = Item(name="Смартфон", price=10000, quantity=20)

    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item = Item(name="Смартфон", price=10000, quantity=20)

    item.pay_rate = 0.8

    item.apply_discount()

    assert item.price == 8000.0

def test_all_items():
    item1 = Item(name="Смартфон", price=10000, quantity=20)
    item2 = Item(name="Ноутбук", price=20000, quantity=5)

    assert Item.all[2:] == [item1, item2]


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')

    assert all(isinstance(item, Item) for item in Item.all)
    assert len(Item.all) == 5


def test_string_to_number():
    numberstring = '10.0'
    int_number = Item.string_to_number(numberstring)

    assert int_number == 10


def test__repr__():
    RPhone = Item(name="RPhone", price=3000000, quantity=3)

    assert repr(RPhone) == "Item('RPhone', 3000000, 3)"


def test__str__():
    Phone = Item(name="GPhone", price=5000000000, quantity=1)

    assert str(Phone) == "GPhone"

def test__magic_methods_Phoneclass__():
    your_phone = Phone("iPhone 14 pro max", 140000, 8, 4)

    assert str(your_phone) == 'iPhone 14 pro max'
    assert repr(your_phone) == "Phone('iPhone 14 pro max', 140000, 8, 4)"

def test__add__():
    item = Item("Gphone", 100000, 11)
    your_phone = Phone("iPhone 14 pro max", 140000, 8, 4)

    assert item + your_phone == 19
    assert your_phone + your_phone == 16
    assert item + item == 22
    assert your_phone + item == 19

def test_number_of_sim():
    your_phone = Phone("iPhone 14 pro max", 140000, 8, 4)

    with pytest.raises(ValueError) as exinfo:
        your_phone.number_of_sim = 0

    assert str(exinfo.value) == "Количество физических SIM-карт должно быть целым числом больше нуля."





