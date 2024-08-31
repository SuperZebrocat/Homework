from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator:
    """Функция фильтрует банковские операции по валюте"""
    filter_result = [x for x in transactions if currency == x["operationAmount"]["currency"]["code"]]
    my_iter = iter(filter_result)
    return my_iter


def transaction_descriptions(transactions: List[Dict]) -> Iterator:
    """Функция выводит описание каждой операции"""
    descriptions_iter = map(lambda x: x.get("description"), transactions)
    for x in descriptions_iter:
        yield x


def card_number_generator(start: int, stop: int) -> Iterator:
    """Функция генерирует номера карт в заданном диапазоне"""
    first_num = 10000000000000000
    start_num = first_num + start
    for i in range(start, stop):
        card_number = str(start_num)
        yield f"{card_number[1:5]} {card_number[5:9]} {card_number[9:13]} {card_number[13:17]}"
        start_num += 1
