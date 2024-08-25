from operator import itemgetter
from typing import Dict, List


def filter_by_state(operation_info_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция для фильтрации операций по состоянию"""
    filtered_list = []
    for operation in operation_info_list:
        if operation["state"] == state:
            filtered_list.append(operation)
    return filtered_list


def sort_by_date(operation_info_list: List[Dict], sort_reverse: bool = True) -> List:
    """Функция сортировки операций по дате в порядке убывания"""
    sorted_list = sorted(operation_info_list, key=itemgetter("date"), reverse=sort_reverse)
    return sorted_list
