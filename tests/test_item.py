"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    item = Item(name="Смартфон", price=10000, quantity=20)

    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item = Item(name="Смартфон", price=10000, quantity=20)
    item.apply_discount()

    assert item.price == 8000.0

def test_all_items():
    item1 = Item(name="Смартфон", price=10000, quantity=20)
    item2 = Item(name="Ноутбук", price=20000, quantity=5)

    assert Item.all[2:] == [item1, item2]





