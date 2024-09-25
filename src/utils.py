import json
import logging
import os
from typing import Any

PATH_FILE = os.path.abspath("../data/operations.json")

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operations_info(path_file: str) -> Any:
    """Функция для получения данных о банковских операциях из JSON-файла"""
    try:
        logger.info(f"Попытка получения данных из файла {path_file}")
        with open(path_file, "r", encoding="utf-8") as file:
            operations = json.load(file)
            logger.info("Данные успешно получены")
            return operations
    except FileNotFoundError:
        logger.error(f'Ошибка получения данных: файл "{path_file}" не найден')
        return []
    except json.JSONDecodeError:
        logger.error(f'Ошибка при чтении json-файла из файла "{path_file}"')
        return []
