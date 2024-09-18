from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [("7000792289606361", "7000 79** **** 6361"), ("", None), ("700079228960", None)],
)
def test_get_mask_card_number(value: str, expected: Any) -> Any:
    """Функция тестирования для функции get_mask_card_number"""
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [("73654108430135874305", "**4305"), ("73654", None), ("", None)],
)
def test_get_mask_account(value: str, expected: Any) -> Any:
    """Функция тестирования для функции get_mask_account"""
    assert get_mask_account(value) == expected
