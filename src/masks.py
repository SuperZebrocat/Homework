import logging
import os
from typing import Any

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)


logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> Any:
    """Функция возвращает маску номера карты"""
    try:
        if len(card_number) == 16:
            logger.info("Маскируем номер карты пользователя")
            return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
        else:
            logger.error("Произошла ошибка: не верный номер карты")
            raise ValueError()
    except ValueError:
        return None


def get_mask_account(account_number: str) -> Any:
    """Функция возвращает маску номера счета"""
    try:
        if len(account_number) == 20:
            logger.info("Маскируем номер счета пользователя")
            return f"**{account_number[-4:]}"
        else:
            logger.error("Произошла ошибка: не верный номер счета")
            raise ValueError()
    except ValueError:
        return None
