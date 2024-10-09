import re
from collections import Counter
from typing import Dict, Iterator, List


def group_by_description(transactions_list: list[dict], user_input: str) -> list:
    """Функция для поиска и группировки банковских операций по описанию"""
    collected_dict_list = []
    for transaction in transactions_list:
        pattern = re.compile(user_input)
        text = str(transaction.get("description"))
        match = pattern.findall(text)
        if match:
            collected_dict_list.append(transaction)
    return collected_dict_list


def filter_by_currency_csv_and_xlsx(transactions: List[Dict], currency: str) -> Iterator:
    """Функция фильтрует банковские операции по валюте"""
    filter_result = [x for x in transactions if currency == x.get("currency_code")]
    my_iter = iter(filter_result)
    return my_iter


def count_by_category(transactions_list: list[dict]) -> dict:
    """Функция для подсчета банковских операций по категориям"""
    category_list = []
    for transaction in transactions_list:
        category_list.append(transaction.get("description"))
    counted = Counter(category_list)
    return dict(counted)
