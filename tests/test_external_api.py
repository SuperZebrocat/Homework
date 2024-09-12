from typing import Dict
from unittest.mock import patch

import pytest

from src.external_api import convert_amount_to_rub


def test_convert_amount_to_rub_empty_dict():
    """Тест работы функции при отсутствии входных данных о транзакции"""
    operation = {}
    with pytest.raises(AttributeError):
        convert_amount_to_rub(operation)


@pytest.mark.parametrize(
    "operation, expected",
    (
        [
            (
                {
                    "id": 633268359,
                    "state": "EXECUTED",
                    "date": "2019-07-12T08:11:47.735774",
                    "operationAmount": {"amount": "2631.44", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Gold 3589276410671603",
                    "to": "Счет 96292138399386853355",
                },
                2631.44,
            )
        ]
    ),
)
def test_convert_amount_to_rub_if_rub(operation: Dict, expected: float):
    """Тест работы функции если валюта операции - рубли"""
    assert convert_amount_to_rub(operation) == expected


@patch("requests.get")
def test_convert_amount_to_rub(mock_get):
    """Тест на обращение к внешнему API для конвертации суммы операции по текущему курсу валют"""
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 49192.52},
        "info": {"timestamp": 1726128315, "rate": 91.694779},
        "date": "2024-09-12",
        "result": 4510697.249853,
    }
    assert convert_amount_to_rub(mock_get) == 4510697.25
    mock_get.assert_called_once()
