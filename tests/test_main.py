import io
from unittest.mock import mock_open, patch

import pytest

from src.main import (
    get_user_description,
    main,
    while_true_currency,
    while_true_description,
    while_true_greeting,
    while_true_sort_by_date,
    while_true_sort_reverse,
    while_true_state,
)


@patch("builtins.input", side_effect=["1"])
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "state": "EXECUTED"}]')
def test_greeting_json(mock_input, mock_file) -> None:
    """Тест получения списка банковских операций из JSON-файла по выбору пользователя"""
    assert while_true_greeting() == ([{"id": 1, "state": "EXECUTED"}], "1")


@patch("builtins.input", side_effect=["2"])
@patch("pandas.read_csv")
def test_greeting_csv(mock_csv, mock_input) -> None:
    """Тест получения списка банковских операций из CSV-файла по выбору пользователя"""
    mock_csv.return_value.to_dict.return_value = [{"transaction": 1}, {"transaction": 2}]
    assert while_true_greeting() == ([{"transaction": 1}, {"transaction": 2}], "2")


@patch("builtins.input", side_effect=["3", "some_input"])
@patch("pandas.read_excel")
def test_greeting_excel(mock_excel, mock_input) -> None:
    """Тест получения списка банковских операций из Excel-файла по выбору пользователя"""
    mock_excel.return_value.to_dict.return_value = [{"transaction": 1}, {"transaction": 2}]
    assert while_true_greeting() == ([{"transaction": 1}, {"transaction": 2}], "3")


@pytest.mark.usefixtures("operation_list_state")
@patch("builtins.input", side_effect=["EXECUTED"])
def test_filter_executed(mock_input, operation_list_state) -> None:
    """Тест фильтрации списка банковских операций по выбранному пользователем статусу 'EXECUTED'"""
    assert while_true_state(operation_list_state) == [{"id": 1, "state": "EXECUTED"}]


@pytest.mark.usefixtures("operation_list_state")
@patch("builtins.input", side_effect=["CANCELED"])
def test_filter_canceled(mock_input, operation_list_state) -> None:
    """Тест фильтрации списка банковских операций по выбранному пользователем статусу 'CANCELED'"""
    assert while_true_state(operation_list_state) == [{"id": 2, "state": "CANCELED"}]


@pytest.mark.usefixtures("operation_list_state")
@patch("builtins.input", side_effect=["PENDING", "some_input"])
def test_filter_pending(mock_input, operation_list_state) -> None:
    """Тест фильтрации списка банковских операций по выбранному пользователем статусу 'PENDING'
    и возрата к выбору статуса при ошибке ввода"""
    assert while_true_state(operation_list_state) == [{"id": 3, "state": "PENDING"}]


@pytest.mark.usefixtures("operation_list_sort_reverse")
@patch("builtins.input", side_effect=["по убыванию"])
def test_sort_reverse_true(mock_input, operation_list_sort_reverse) -> None:
    """Тест сортировку списка банковских операций по дате в направлении убывания"""
    assert while_true_sort_reverse(operation_list_sort_reverse) == [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.usefixtures("operation_list_sort_reverse")
@patch("builtins.input", side_effect=["по возрастанию", "some_input"])
def test_sort_reverse_false(mock_input, operation_list_sort_reverse) -> None:
    """Тест сортировку списка банковских операций по дате в направлении возрастания"""
    assert while_true_sort_reverse(operation_list_sort_reverse) == [
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.usefixtures("operation_list_sort_reverse")
@patch("builtins.input", side_effect=["да", "по убыванию"])
def test_sort_by_date_reverse_true(mock_input, operation_list_sort_reverse) -> None:
    """Тест сортировку списка банковских операций по дате в выбранном пользователем направлении"""
    assert while_true_sort_by_date(operation_list_sort_reverse) == [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.usefixtures("operation_list_sort_reverse")
@patch("builtins.input", side_effect=["да", "по возрастанию"])
def test_sort_by_date_reverse_false(mock_input, operation_list_sort_reverse) -> None:
    """Тест сортировку списка банковских операций по дате в выбранном пользователем направлении"""
    assert while_true_sort_by_date(operation_list_sort_reverse) == [
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.usefixtures("operation_list_sort_reverse")
@patch("builtins.input", side_effect=["нет", "some_input"])
def test_unsorted_by_date(mock_input, operation_list_sort_reverse) -> None:
    """Тест возврата неотсортированного по дате списка банковских операций в соответствии выбору пользователя"""
    assert while_true_sort_by_date(operation_list_sort_reverse) == [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.mark.usefixtures("operation_list_currency_json")
@patch("builtins.input", side_effect=["да"])
def test_filtered_by_currency_json(mock_input, operation_list_currency_json) -> None:
    """Тест на фильтрацию списка банковких операций по валюте 'рубли' из JSON-файла"""
    assert while_true_currency(operation_list_currency_json, "1") == [
        {"id": 2, "operationAmount": {"amount": "2000", "currency": {"name": "руб.", "code": "RUB"}}},
        {"id": 4, "operationAmount": {"amount": "4000", "currency": {"name": "руб.", "code": "RUB"}}},
    ]


@pytest.mark.usefixtures("operation_list_currency_json")
@patch("builtins.input", side_effect=["нет", "some_input"])
def test_unfiltered_by_currency_json(mock_input, operation_list_currency_json) -> None:
    """Тест возврата неотсортированного по валюте списка банковских операций
    из JSON-файла в соответствии выбору пользователя"""
    assert while_true_currency(operation_list_currency_json, "1") == [
        {"id": 1, "operationAmount": {"amount": "1000", "currency": {"name": "EUR", "code": "EUR"}}},
        {"id": 2, "operationAmount": {"amount": "2000", "currency": {"name": "руб.", "code": "RUB"}}},
        {"id": 3, "operationAmount": {"amount": "3000", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 4, "operationAmount": {"amount": "4000", "currency": {"name": "руб.", "code": "RUB"}}},
    ]


@pytest.mark.usefixtures("transactions_csv_xlsx")
@patch("builtins.input", side_effect=["да"])
def test_filtered_by_currency_csv(mock_input, transactions_csv_xlsx) -> None:
    """Тест на фильтрацию списка банковких операций по валюте 'рубли' из CSV-файла"""
    assert while_true_currency(transactions_csv_xlsx, "2") == [
        {"id": 4234093.0, "state": "EXECUTED", "currency_code": "RUB"}
    ]


@pytest.mark.usefixtures("transactions_csv_xlsx")
@patch("builtins.input", side_effect=["нет", "some_input"])
def test_unfiltered_by_currency_csv(mock_input, transactions_csv_xlsx) -> None:
    """Тест возврата неотсортированного по валюте списка банковских операций
    из CSV-файла в соответствии выбору пользователя"""
    assert while_true_currency(transactions_csv_xlsx, "2") == [
        {"id": 3176764.0, "state": "CANCELED", "currency_code": "EUR"},
        {"id": 4234093.0, "state": "EXECUTED", "currency_code": "RUB"},
        {"id": 3107343.0, "state": "EXECUTED", "currency_code": "SEK"},
        {"id": 2130098.0, "state": "PENDING", "currency_code": "EUR"},
        {"id": 4653427.0, "state": "PENDING", "currency_code": "CNY"},
        {"id": 4641894.0, "state": "EXECUTED", "currency_code": "SEK"},
    ]


@pytest.mark.usefixtures("transactions_csv_xlsx")
@patch("builtins.input", side_effect=["да"])
def test_filtered_by_currency_xlsx(mock_input, transactions_csv_xlsx) -> None:
    """Тест на фильтрацию списка банковких операций по валюте 'рубли' из CSV-файла"""
    assert while_true_currency(transactions_csv_xlsx, "3") == [
        {"id": 4234093.0, "state": "EXECUTED", "currency_code": "RUB"}
    ]


@pytest.mark.usefixtures("transactions_csv_xlsx")
@patch("builtins.input", side_effect=["нет", "some_input"])
def test_unfiltered_by_currency_xlsx(mock_input, transactions_csv_xlsx) -> None:
    """Тест возврата неотсортированного по валюте списка банковских операций
    из Excel-файла в соответствии выбору пользователя"""
    assert while_true_currency(transactions_csv_xlsx, "3") == [
        {"id": 3176764.0, "state": "CANCELED", "currency_code": "EUR"},
        {"id": 4234093.0, "state": "EXECUTED", "currency_code": "RUB"},
        {"id": 3107343.0, "state": "EXECUTED", "currency_code": "SEK"},
        {"id": 2130098.0, "state": "PENDING", "currency_code": "EUR"},
        {"id": 4653427.0, "state": "PENDING", "currency_code": "CNY"},
        {"id": 4641894.0, "state": "EXECUTED", "currency_code": "SEK"},
    ]


@pytest.mark.usefixtures("operation_list_description")
@patch("builtins.input", side_effect=["да", "вклад"])
def test_filtered_by_description(mock_input, operation_list_description) -> None:
    """Тест на фильтрацию списка банковких операций по категории"""
    assert while_true_description(operation_list_description) == [{"id": 2, "description": "Открытие вклада"}]


@pytest.mark.usefixtures("operation_list_description")
@patch("builtins.input", side_effect=["нет", "some_input"])
def test_unfiltered_by_description(mock_input, operation_list_description) -> None:
    """Тест возрата неотфильтрованного по категории списка банковких операций"""
    assert while_true_description(operation_list_description) == [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод с карты на карту"},
    ]


@patch("builtins.input", side_effect=["вклад"])
def test_get_description(mock_input) -> None:
    """Функция получения от пользователя ключевого слова для фильтрации списка банковских операций по категории"""
    assert get_user_description() == "вклад"


@pytest.mark.usefixtures("mock_operations")
@patch("src.main.while_true_description")
@patch("sys.stdout", new_callable=io.StringIO)
@patch("builtins.input", side_effect=["1", "EXECUTED", "нет", "нет", "нет"])
def test_main(mock_input, mock_stdout, mock_while_true_description, mock_operations) -> None:
    """Тест вывода в консоль окончательно сформированного после фильтрации списка банковских операций"""
    mock_while_true_description.return_value = mock_operations
    main()
    output = mock_stdout.getvalue()
    expected_output = (
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Для обработки выбран JSON-файл.\n"
        "Операции отфильтрованы по статусу 'EXECUTED'\n"
        "Распечатываю итоговый список транзакций...\n"
        "Всего банковских операций в выборке: 2\n"
        "\n1. 23.03.2019 Перевод со счета на счет\n"
        "Счет **4719 -> Счет **1160\n"
        "Сумма: 1000.0 руб.\n"
        "\n2. 20.12.2018 Перевод организации\n"
        "Счет **5355 -> Счет **6366\n"
        "Сумма: 2000.0 USD\n"
    )
    assert output == expected_output


@patch("src.main.while_true_description")
@patch("sys.stdout", new_callable=io.StringIO)
@patch("builtins.input", side_effect=["1", "CANCELED", "нет", "нет", "нет"])
def test_main_empty_list(mock_input, mock_stdout, mock_while_true_description) -> None:
    """Тест вывода в консоль сообщения, если список отфильрованных банковских операций пуст"""
    mock_while_true_description.return_value = []

    main()
    output = mock_stdout.getvalue()
    expected_output = (
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Для обработки выбран JSON-файл.\n"
        "Операции отфильтрованы по статусу 'CANCELED'\n"
        "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"
    )
    assert output == expected_output
