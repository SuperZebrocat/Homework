import os
import re
from typing import Any

from src.dataframe import read_data_csv, read_data_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.searching import filter_by_currency_csv_and_xlsx, group_by_description
from src.utils import get_operations_info
from src.widget import mask_account_card

PATH_FILE_JSON = os.path.abspath("data/operations.json")
PATH_FILE_CSV = os.path.abspath("../data/transactions.csv")
PATH_FILE_EXCEL = os.path.abspath("../data/transactions_excel.xlsx")


def main() -> None:
    """Функция выводит список банковских транзакций согласно фильтрации, выбранной пользователем"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    def while_true_greeting() -> tuple[list[Any], str]:
        operation_list = []
        while True:
            user_input_greeting = input(
                "Выберите необходимый пункт меню:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла\n"
            )
            if user_input_greeting in ["1", "2", "3"]:
                if user_input_greeting == "1":
                    print("Для обработки выбран JSON-файл.")
                    operation_list = get_operations_info(PATH_FILE_JSON)
                elif user_input_greeting == "2":
                    print("Для обработки выбран CSV-файл.")
                    operation_list = read_data_csv(PATH_FILE_CSV)
                elif user_input_greeting == "3":
                    print("Для обработки выбран XLSX-файл.")
                    operation_list = read_data_excel(PATH_FILE_EXCEL)
                break
            else:
                print(f"Пункт меню '{user_input_greeting}' не существует. Повторите попытку.")
                continue
        return operation_list, user_input_greeting

    operations, user_choice_greeting = while_true_greeting()

    def while_true_state() -> list:
        filtered_list = []
        while True:
            state_list = ["EXECUTED", "CANCELED", "PENDING"]
            user_input_state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            if user_input_state.upper() in state_list:
                print(f"Операции отфильтрованы по статусу '{user_input_state.upper()}'")
                state = user_input_state.upper()
                filtered_list = filter_by_state(operations, state)
                break
            elif user_input_state.upper() not in state_list:
                print(f"Статус операции '{user_input_state}' недоступен.")
                continue
        return filtered_list

    filtered_list_by_state = while_true_state()

    def while_true_sort_by_date() -> list:
        sorted_list = []
        while True:
            user_input_sort_by_date = input("Отсортировать операции по дате? Да/Нет\n")
            if user_input_sort_by_date.lower() in ["да", "нет"]:
                if user_input_sort_by_date.lower() == "да":

                    def while_true_sort_reverse() -> list:
                        sorted_list_reverse = []
                        while True:
                            user_input_sort_reverse = input("Отсортировать по возрастанию или по убыванию?\n")
                            if user_input_sort_reverse.lower() in ["по возрастанию", "по убыванию"]:
                                if user_input_sort_reverse.lower() == "по возрастанию":
                                    sorted_list_reverse = sort_by_date(filtered_list_by_state, sort_reverse=False)
                                elif user_input_sort_reverse.lower() == "по убыванию":
                                    sorted_list_reverse = sort_by_date(filtered_list_by_state, sort_reverse=True)
                                break
                            else:
                                print("Ожидаемый ответ: по возрастанию/по убыванию. Попробуйте еще раз.")
                                continue
                        return sorted_list_reverse

                    sorted_list = while_true_sort_reverse()
                elif user_input_sort_by_date.lower() == "нет":
                    sorted_list = filtered_list_by_state
                break
            else:
                print("Ожидаемый ответ: Да/Нет. Попробуйте еще раз.")
                continue
        return sorted_list

    sorted_list_by_date = while_true_sort_by_date()

    def while_true_currency() -> list:
        filtered_list_by_currency = []
        while True:
            user_input_currency = input("Выводить только рублевые транзакции? Да/Нет\n")
            if user_input_currency.lower() in ["да", "нет"]:
                if user_input_currency.lower() == "да":
                    if user_choice_greeting == "1":
                        filtered_list_by_currency = list(filter_by_currency(sorted_list_by_date, "RUB"))
                    elif user_choice_greeting in ["2", "3"]:
                        filtered_list_by_currency = list(filter_by_currency_csv_and_xlsx(sorted_list_by_date, "RUB"))
                elif user_input_currency.lower() == "нет":
                    filtered_list_by_currency = sorted_list_by_date
                break
            else:
                print("Ожидаемый ответ: Да/Нет. Попробуйте еще раз.")
                continue
        return filtered_list_by_currency

    filtered_by_currency = while_true_currency()

    def while_true_description() -> list:
        filtered_list_by_description = []
        while True:
            user_input_filter_by_description = input(
                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
            )
            if user_input_filter_by_description.lower() in ["да", "нет"]:
                if user_input_filter_by_description.lower() == "да":
                    get_user_description = input("Введите слово для фильтрации по описанию\n")
                    filtered_list_by_description = group_by_description(filtered_by_currency, get_user_description)
                elif user_input_filter_by_description.lower() == "нет":
                    filtered_list_by_description = filtered_by_currency
                break
            else:
                print("Ожидаемый ответ: Да/Нет. Попробуйте еще раз.")
                continue
        return filtered_list_by_description

    filtered_by_description = while_true_description()
    normalized_date = ""
    if len(filtered_by_description) > 0:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_by_description)}")
        pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
        counter = 0
        for operation in filtered_by_description:
            counter += 1
            operation_date = operation.get("date")
            match = pattern.search(operation_date)
            if match:
                normalized_date = f"{match.group(3)}.{match.group(2)}.{match.group(1)}"
            operation_description = operation.get("description")
            if user_choice_greeting == "1":
                operation_sum = operation.get("operationAmount").get("amount")
                operation_currency = operation.get("operationAmount").get("currency").get("name")
            else:
                operation_sum = operation.get("amount")
                operation_currency = operation.get("currency_name")
            operation_from = mask_account_card(operation.get("from"))
            operation_to = mask_account_card(operation.get("to"))
            if operation_from and operation_to:
                print(
                    f"\n{counter}. {normalized_date} {operation_description}\n{operation_from} -> {operation_to}\n"
                    f"Сумма: {operation_sum} {operation_currency}"
                )
            else:
                print(
                    f"\n{counter} {normalized_date} {operation_description}\n{operation_to}\n"
                    f"Сумма: {operation_sum} {operation_currency}"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
