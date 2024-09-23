import os
from typing import Any

import pandas as pd

PATH_FILE_CSV = os.path.abspath("../data/transactions.csv")
PATH_FILE_EXCEL = os.path.abspath("../data/transactions_excel.xlsx")


def read_data_csv(file_path: Any) -> Any:
    """Функция для считывания финансовых операций из CSV-файла"""
    try:
        df_csv = pd.read_csv(file_path, delimiter=";")
        transactions_csv = df_csv.to_dict(orient="records")
        return transactions_csv
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        return []
    except ValueError:
        return []


def read_data_excel(file_path: Any) -> Any:
    """Функция для считывания финансовых операций из Excel-файла"""
    try:
        df_excel = pd.read_excel(file_path)
        transactions_excel = df_excel.to_dict(orient="records")
        return transactions_excel
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        return []
    except ValueError:
        return []
