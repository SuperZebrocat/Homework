import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_amount_to_rub(operation: Dict) -> float:
    """Функция конвертации суммы банковских операций в рубли"""
    try:
        currency = operation.get("operationAmount").get("currency").get("code")
        amount = operation.get("operationAmount").get("amount")
    except AttributeError:
        raise AttributeError
    if currency != "RUB":
        try:
            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {
                "amount": amount,
                "from": currency,
                "to": "RUB",
            }
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()
            result = response.json()
            print(result)
            return round(result["result"], 2)
        except requests.exceptions.RequestException:
            print("An error occurred. Please try again later.")
    else:
        return float(amount)
