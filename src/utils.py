import json
import os
from typing import List

PATH_FILE = os.path.abspath("../data/operations.json")


def get_operations_info(path_file: str) -> List:
    """Функция для получения данных о банковских операциях из JSON-файла"""
    try:
        with open(path_file, "r", encoding="utf-8") as file:
            operations = json.load(file)
            return operations
    except FileNotFoundError:
        print(f'Ошибка: файл "{path_file}" не найден')
        return []
    except json.JSONDecodeError:
        print(f'Ошибка при чтении json-файла из файла "{path_file}"')
        return []
