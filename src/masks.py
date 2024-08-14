def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты"""
    # card_number_for_mask = str(card_number)
    # return f"{card_number_for_mask[0:4]} {card_number_for_mask[4:6]}** **** {card_number_for_mask[12:16]}"
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает маску номера счета"""
    # account_number_for_mask = str(account_number)
    # return f"**{account_number_for_mask[-4:]}"
    return f"**{account_number[-4:]}"
