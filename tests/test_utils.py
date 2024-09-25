from unittest.mock import mock_open, patch

from src.utils import get_operations_info


@patch("builtins.open", new_callable=mock_open, read_data='[{"transaction_id": 1}]')
def test_get_operations_info(mock_file):
    """Тест на корректность чтения данных из json-файла"""
    operations = get_operations_info(mock_file)
    assert operations == [{"transaction_id": 1}]


@patch("builtins.open", new_callable=mock_open, read_data="I am not json")
def test_get_operations_info_not_json(mock_file):
    """Тест работы функции если json-файл пуст или данные не соответствуют формату json"""
    operations = get_operations_info(mock_file)
    assert operations == []


def test_get_operations_info_file_not_found():
    """Тест работы функции, если json-файл не найден"""
    path_file = "no_file.json"
    assert get_operations_info(path_file) == []
