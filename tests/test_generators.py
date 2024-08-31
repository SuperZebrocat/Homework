from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions: List[Dict], currency: str, expected: List[Dict]) -> None:
    assert list(filter_by_currency(transactions, currency)) == expected


def test_filter_by_currency_empty_list(transactions: List[Dict]) -> None:
    empty_transactions_list: List[Dict] = []
    with pytest.raises(StopIteration):
        next(filter_by_currency(empty_transactions_list, "USD"))


def test_transaction_descriptions(transactions: List[Dict]) -> None:
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_empty_list(transactions: List[Dict]) -> None:
    empty_transactions_list: List[Dict] = []
    descriptions = transaction_descriptions(empty_transactions_list)
    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator() -> None:
    card_number = card_number_generator(2200220022002200, 2200220022002205)
    assert next(card_number) == "2200 2200 2200 2200"
    assert next(card_number) == "2200 2200 2200 2201"
    assert next(card_number) == "2200 2200 2200 2202"
    assert next(card_number) == "2200 2200 2200 2203"
    assert next(card_number) == "2200 2200 2200 2204"


def test_card_number_generator_stop_iteration() -> None:
    card_number = card_number_generator(2200220022002200, 2200220022002201)
    with pytest.raises(StopIteration):
        next(card_number)
        next(card_number)
