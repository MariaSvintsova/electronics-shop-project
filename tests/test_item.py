"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


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
    list_of_items = Item.instantiate_from_csv('../src/items.csv')

    assert all(isinstance(item, Item) for item in list_of_items)
    assert len(list_of_items) == 5


def test_string_to_number():
    numberstring = '10.0'
    int_number = Item.string_to_number(numberstring)

    assert int_number == 10


