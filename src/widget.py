from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция возвращает информацию о картах/счетах с замаскированным номером"""
    user_input_for_mask = user_input.split()
    if len(user_input_for_mask[-1]) == 16:
        masked_number = get_mask_card_number(user_input_for_mask[-1])
        user_input_for_mask[-1] = masked_number
    elif len(user_input_for_mask[-1]) == 20:
        masked_number = get_mask_account(user_input_for_mask[-1])
        user_input_for_mask[-1] = masked_number
    return " ".join(user_input_for_mask)


def get_date(user_date: str) -> str:
    """Фуyкция для вывода даты в формате 'ДД.ММ.ГГГГ'"""
    date_for_format = user_date[0:10].split("-")
    return ".".join(date_for_format[::-1])
