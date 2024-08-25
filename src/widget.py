from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> Any:
    """Функция возвращает информацию о картах/счетах с замаскированным номером"""
    user_input_for_mask = user_input.split()
    if len(user_input_for_mask) > 1 and len(user_input_for_mask[-1]) == 16:
        masked_number = get_mask_card_number(user_input_for_mask[-1])
        if masked_number is not None:
            user_input_for_mask[-1] = masked_number
            return " ".join(user_input_for_mask)
    elif len(user_input_for_mask) > 1 and len(user_input_for_mask[-1]) == 20:
        masked_number = get_mask_account(user_input_for_mask[-1])
        if masked_number is not None:
            user_input_for_mask[-1] = masked_number
            return " ".join(user_input_for_mask)
    else:
        return "Ошибка ввода данных"


def get_date(user_date: str) -> Any:
    """Фуyкция для вывода даты в формате 'ДД.ММ.ГГГГ'"""
    date_for_format = user_date[0:10].split("-")
    if len(user_date) >= 10 and len(date_for_format) == 3:
        return ".".join(date_for_format[::-1])
    else:
        return "Неверно задана дата"
