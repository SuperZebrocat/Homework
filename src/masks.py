def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    else:
        return "Неверно введен номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает маску номера счета"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Неверно введен номер счета"
