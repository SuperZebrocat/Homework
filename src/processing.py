from operator import itemgetter


def filter_by_state(operation_info_list: list, state="executed") -> list:
    """Функция для фильтрации операций по состоянию"""
    filtered_list = []
    for operation in operation_info_list:
        if operation.get("state").lower() == state:
            filtered_list.append(operation)
    return filtered_list
