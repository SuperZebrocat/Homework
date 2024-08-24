import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("hello", "Неверно введен номер карты"),
        ("", "Неверно введен номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_card_number_not_str():
    with pytest.raises(TypeError):
        get_mask_card_number(123)


@pytest.mark.parametrize(
    "value, expected",
    [("73654108430135874305", "**4305"), ("hello", "Неверно введен номер счета"), ("", "Неверно введен номер счета")],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_not_str():
    with pytest.raises(TypeError):
        get_mask_card_number(123)
