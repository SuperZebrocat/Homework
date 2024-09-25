import io
from typing import Any
from unittest.mock import patch

from src.dataframe import read_data_csv, read_data_excel


@patch("pandas.read_csv")
def test_read_data_csv(mock_csv: Any) -> None:
    """Тест на корректность чтения данных из csv-файла"""
    mock_csv.return_value.to_dict.return_value = [{"transaction": 1}, {"transaction": 2}]
    assert read_data_csv(file_path="test.csv") == [{"transaction": 1}, {"transaction": 2}]
    mock_csv.assert_called_with("test.csv", delimiter=";")


def test_read_data_csv_file_not_found() -> None:
    """Тест работы функции в случае, если csv-файл не найден"""
    file_path = "no_file"
    assert read_data_csv(file_path) == []


def test_read_data_csv_empty_file() -> None:
    """Тест работы функции в случае, если csv-файл пуст"""
    empty_file = io.StringIO()
    assert read_data_csv(empty_file) == []


@patch("pandas.read_excel")
def test_read_data_excel(mock_excel: Any) -> None:
    """Тест на корректность чтения данных из excel-файла"""
    mock_excel.return_value.to_dict.return_value = [{"transaction": 1}, {"transaction": 2}]
    assert read_data_excel(file_path="test.xlsx") == [{"transaction": 1}, {"transaction": 2}]
    mock_excel.assert_called_with("test.xlsx")


def test_read_data_excel_file_not_found() -> None:
    """Тест работы функции в случае, если excel-файл не найден"""
    file_path = "no_file"
    assert read_data_excel(file_path) == []


def test_read_data_excel_empty_file() -> None:
    """Тест работы функции в случае, если excel-файл пуст"""
    empty_file = io.StringIO()
    assert read_data_excel(empty_file) == []
