from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("", []),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(bank_operation_info: List[Dict], state: str, expected: List[Dict]) -> None:
    """Функция для тестирования функции filter_by_state"""
    assert filter_by_state(bank_operation_info, state) == expected


@pytest.mark.parametrize(
    "sort_reverse, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(operations_for_test: List[Dict], sort_reverse: bool, expected: List[Dict]) -> None:
    assert sort_by_date(operations_for_test, sort_reverse) == expected


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []


def test_sort_by_date_if_same_dates() -> None:
    same_dates_operations = [
        {"id": 1, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]

    assert sort_by_date(same_dates_operations) == [
        {"id": 4, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 1, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
