from typing import List

import pytest


@pytest.fixture
def bank_operation_info() -> List:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_for_test() -> List:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions() -> List:
    return [
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
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
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
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_csv_xlsx() -> List:
    return [
        {"id": 3176764.0, "state": "CANCELED", "currency_code": "EUR"},
        {"id": 4234093.0, "state": "EXECUTED", "currency_code": "RUB"},
        {"id": 3107343.0, "state": "EXECUTED", "currency_code": "SEK"},
        {"id": 2130098.0, "state": "PENDING", "currency_code": "EUR"},
        {"id": 4653427.0, "state": "PENDING", "currency_code": "CNY"},
        {"id": 4641894.0, "state": "EXECUTED", "currency_code": "SEK"},
    ]


@pytest.fixture
def operation_list_state() -> list:
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "PENDING"},
    ]


@pytest.fixture
def operation_list_sort_reverse() -> list:
    return [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def operation_list_currency_json() -> List:
    return [
        {"id": 1, "operationAmount": {"amount": "1000", "currency": {"name": "EUR", "code": "EUR"}}},
        {"id": 2, "operationAmount": {"amount": "2000", "currency": {"name": "руб.", "code": "RUB"}}},
        {"id": 3, "operationAmount": {"amount": "3000", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 4, "operationAmount": {"amount": "4000", "currency": {"name": "руб.", "code": "RUB"}}},
    ]


@pytest.fixture
def operation_list_description() -> List:
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def mock_operations() -> List:
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "1000.0", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "2000.0", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
    ]
