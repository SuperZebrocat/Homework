from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Ошибка ввода данных"),
        ("Счет", "Ошибка ввода данных"),
        ("Visa Platinum", "Ошибка ввода данных"),
        ("73654108430135874305", "Ошибка ввода данных"),
        ("Visa Platinum 700079228960636", "Ошибка ввода данных"),
    ],
)
def test_mask_account_card(value: str, expected: Any) -> None:
    """Функция тестирования функции mask_account_card"""
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", "Неверно задана дата"),
        ("2024-03-11", "11.03.2024"),
        ("2024-032311554478411", "Неверно задана дата"),
    ],
)
def test_get_date(value: str, expected: Any) -> None:
    """Функция тестирования функции get_date"""
    assert get_date(value) == expected
