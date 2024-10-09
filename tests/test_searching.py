import pytest

from src.searching import count_by_category, filter_by_currency_csv_and_xlsx, group_by_description


@pytest.mark.parametrize(
    "user_input, expected",
    [
        (
            "Перевод организации",
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
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        )
    ],
)
def test_group_by_description(transactions: list[dict], user_input: str, expected: list[dict]) -> None:
    """Тестирование работы функции по поиску и группировке банковских операций по описанию"""
    assert group_by_description(transactions, user_input) == expected


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "EUR",
            [
                {"id": 3176764.0, "state": "CANCELED", "currency_code": "EUR"},
                {"id": 2130098.0, "state": "PENDING", "currency_code": "EUR"},
            ],
        ),
        ("RUB", [{"id": 4234093.0, "state": "EXECUTED", "currency_code": "RUB"}]),
    ],
)
def test_filter_by_currency_csv_xlsx(transactions_csv_xlsx: list[dict], currency: str, expected: list[dict]) -> None:
    assert list(filter_by_currency_csv_and_xlsx(transactions_csv_xlsx, currency)) == expected


def test_count_by_category(transactions: list[dict]) -> None:
    assert count_by_category(transactions) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }
